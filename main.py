import warnings
warnings.filterwarnings('ignore')
from crewai import Agent, Crew, Task,LLM,Process
from utils import get_gemini_api_key
from tools import GmailTool,Read_Pdf
from crewai_tools import ScrapeWebsiteTool
import os


gmail_tool = GmailTool()
read_pdf = Read_Pdf()
scrapper = ScrapeWebsiteTool()

model= get_gemini_api_key()
gemini_api_key = os.getenv("GOOGLE_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

# Use Gemini 2.5 Pro Experimental model
gemini_llm = LLM(
    model='gemini/gemini-1.5-flash', 
    api_key=gemini_api_key,
    temperature=0.1 # Lower temperature for more factual analysis
)    
resume_extractor = Agent(
    role="Resume Extractor",
    goal="You are a resume extractor. Using GmailTool, you will extract resumes from the inbox and then extract github links from the resumes using readpdf tool.\ " \
    "You will return the results in a structured format. \n filename: [name of file], github link: [extracted github link]",
    backstory="Your are a expert in extracting information from resumes. You will use GmailTool to fetch resumes from the inbox and then use readpdf tool to extract github links from the resumes.\
         resumes are stored in the 'Resumes' folder for file name refer to files variable returned by gmail tool. You will return the results in a structured format.",
    llm=gemini_llm,
    tools=[
        gmail_tool,
        read_pdf,
    ],
    verbose=True,
    allow_delegation=True,
    memory=True
)

resume_task = Task(
    name="Resume Extraction Task",
    agent=resume_extractor,
    tools=[
        gmail_tool,
        read_pdf,
    ],
    description=("Extract github links from the resumes files."),
    expected_output=("GIve the output in the following format:\n"
        "filename: <filename>, github link: <github_link>\n"
        "If no github link is found, return 'No github link found'.\n"
        "If no resumes are found, leave blank.\n" \
        "if error occurs, return 'Error occurred while extracting resumes.'\n" \
    ),
)

Github_Analyser = Agent(
    role="Github Analysis",
    goal="You are a github analysis agent.You will get the github link by resume extractor in the format filename: [name of file], github link: [github link] \
        You will analyze the github links extracted from the resumes and provide insights.\
        also check for the pull requests, issues, and contributions in the github profile. and make sure to include it everytime and give \
            the output in the form of well written markdown report containing the file name github link and extracted insights int the form of table.",
    backstory="You are an expert in analyzing github profiles. You will analyze the github links extracted from the resumes and provide insights.",
    llm=gemini_llm,
    tools=[scrapper],
    verbose=True,
    memory=True
)
github_task=Task(
    name="Github Analysis Task",
    agent=Github_Analyser,
    tools=[
        scrapper,
    ],
    description=("Analyze the github links extracted from the resumes and provide insights. if no output is found, return 'No output found'."
    "use https://github-readme-stats.vercel.app/api?username=[github_username]&show_icons=true&theme=radical for github stats. and also check for github id of user provided by resume extractor."),
    expected_output=("Give the output in the form of well written report file containing the file name, github link and extracted insights in the report form.\n"),
    output_file='report.docx'
)

crew = Crew(
    agents=[resume_extractor, Github_Analyser],
    tasks=[resume_task, github_task],
    verbose=True,
    # process=Process.sequential
    # memory=True,  # Enable memory to retain context across tasks

)

result=crew.kickoff()
print(result)