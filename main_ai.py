
#import C:\\Users\\scott\\OneDrive\\Documents\\GitHub\\ResumeGPT2\\services\\resume_improver


import os, sys
os.chdir('C:\\Users\\scott\\OneDrive\\Documents\\GitHub\\ResumeGPT')
sys.path.insert(0, os.path.abspath(".."))
#sys.path.insert(0,'C:\\Users\\scott\\OneDrive\\Documents\\GitHub\\ResumeGPT')


import ResumeGPT


url = "G:\\My Drive\\pers\\hunt25\\Zillow Principal Applied Scientist Experimentation.html"
#url = "https://zillow.wd5.myworkdayjobs.com/en-US/Zillow_Group_External/details/Principal-Applied-Scientist--Experimentation_P747055"
resume_improver = ResumeGPT.services.ResumeImprover(url)
resume_improver.url = url
resume_improver.create_draft_tailored_resume()
