from com.github import repository
from com.github import db
from linuxtips import sounds
from repo import config
from datetime import datetime
import os, random, sys, getopt

argumentList = sys.argv[1:]
repo_name    = config.Config().Return('reponame')
gh_user      = config.Config().Return('user')
gh_token     = config.Config().Return('token')
repo         = repository.Github(repo_name,gh_user,gh_token)


options      = "sfipqr"
long_options = ["stars", "forks", "issues", "pullrequest", "pullrequestcount", "repository"]

try:
    # Initialize DataBase and create him if not exist
    db.DataBase() 
    
    # start
    arguments, values = getopt.getopt(argumentList, options, long_options)
    
    for currentArgument, currentValue in arguments:
        
        if currentArgument in ("-s", "--stars"):
            
            stars         = repo.GetAtributes('stars')
            stars_data_db = db.DataBase().checkStatus('stars')
            now           = datetime.now()
            notification  = sounds.BadTux().Notification(1)
            stars_data    = (stars,now.strftime("%Y-%m-%dT%H:%M:%SZ"))
            
            if stars_data_db == None:
                
                if stars > 0:
                    
                    db.DataBase().populeStatus('stars', stars_data)
                    print(stars)
                else:
                    print(stars)
                
            elif int(stars) > int(stars_data_db):
                
                notification  = sounds.BadTux().Notification(1)
                
                print(stars)
                db.DataBase().populeStatus('stars', stars_data)
                os.system("mpg123 " + " -q " + notification)
            
            elif int(stars) == int(stars_data_db):
                
                print(stars)
                    
        elif currentArgument in ("-i", "--issues"):
            
            issues         = repo.GetAtributes('issues')
            issues_data_db = db.DataBase().checkStatus('issues')
            now            = datetime.now()
            notification   = sounds.BadTux().Notification(2)
            issues_data    = (issues,now.strftime("%Y-%m-%dT%H:%M:%SZ"))
           
            if issues_data_db == None:
                
                if issues > 0:
                    db.DataBase().populeStatus('issues', issues_data)
                    print(issues)
                    os.system("mpg123 " + " -q " + notification)
                else:
                    print(issues)
                
            elif int(issues) > int(issues_data_db):
                
                notification  = sounds.BadTux().Notification(2)
                
                print(issues)
                db.DataBase().populeStatus('stars', issues_data)
                os.system("mpg123 " + " -q " + notification)
            
            elif int(issues) == int(issues_data_db):
                
                print(issues)
        
        elif currentArgument in ("-f", "--forks"):
            
            forks         = repo.GetAtributes('forks')
            forks_db_data = db.DataBase().checkStatus('forks')
            now           = datetime.now()
            notification  = sounds.BadTux().Notification(3)
            forks_data    = (forks,now.strftime("%Y-%m-%dT%H:%M:%SZ"))
            
            if forks_db_data == None:
                
                
                if forks > 0:
                    db.DataBase().populeStatus('forks', forks_data)
                    print(forks)
                    os.system("mpg123 " + " -q " + notification)
                else:
                    print(forks)
                
            elif int(forks) > int(forks_db_data):
                
                notification  = sounds.BadTux().Notification(3)
                
                print(issues)
                db.DataBase().populeStatus('forks', forks_data)
                os.system("mpg123 " + " -q " + notification)
            
            elif int(forks) == int(forks_db_data):
                
                print(forks)
                
        elif currentArgument in ("-p", "--pullrequest"):
            
            pr           = repo.GetAtributes('pr')
            prc          = repo.GetAtributes('prc')
            
            if len(prc) != 0:
                
                pr_db_total = db.DataBase().checkPullRequestsCount()[0]
                
                if len(prc) > pr_db_total:
                    
                    for i in pr:
                        
                        pr_exist = db.DataBase().checkPullRequestsID(i['pr_id'])
                        
                        if pr_exist == None:
                            
                            pr_data  = i['pr_id'],i['repository'],i['created_at'],i['title']
                            db.DataBase().populePullRequests(pr_data)
                            
                    notification = sounds.BadTux().Notification(4)
                    os.system("mpg123 " + " -q " + notification)
                    last_pr   = db.DataBase().checkPullRequests()
                    last_id   = last_pr[0]
                    last_title= last_pr[3]
                    print(last_id,last_title)
                    
                elif prc == pr_db_total:
                    
                    last_pr   = db.DataBase().checkPullRequests()
                    last_id   = last_pr[0]
                    last_repo = last_pr[1]
                    last_date = last_pr[2]
                    last_title= last_pr[3]
                    print(last_id,last_title)
            else:
                print("Sem Novos Pull Requests")
        
        elif currentArgument in ("-q", "--pullrequestcount"):
            
            pr           = repo.GetAtributes('pr')
            prc          = repo.GetAtributes('prc')
            
            if len(prc) != 0:
                
                pr_db_total = db.DataBase().checkPullRequestsCount()[0]
                
                if len(prc) > pr_db_total:
                    
                    for i in pr:
                        
                        pr_exist = db.DataBase().checkPullRequestsID(i['pr_id'])
                        
                        if pr_exist == None:
                            
                            pr_data  = i['pr_id'],i['repository'],i['created_at'],i['title']
                            db.DataBase().populePullRequests(pr_data)
                            
                    notification = sounds.BadTux().Notification(4)
                    os.system("mpg123 " + " -q " + notification)
                    last_pr   = db.DataBase().checkPullRequests()
                    last_id   = last_pr[0]
                    last_title= last_pr[3]
                    print(db.DataBase().checkPullRequestsCount()[0])
                    
                elif prc == pr_db_total:
                    
                    last_pr   = db.DataBase().checkPullRequests()
                    last_id   = last_pr[0]
                    last_repo = last_pr[1]
                    last_date = last_pr[2]
                    last_title= last_pr[3]
                    print(db.DataBase().checkPullRequestsCount()[0])
            else:
                print("0")
        
        elif currentArgument in ("-r", "--repository"):
            
            print(repo_name)
                
except getopt.error as err:
    print(err)