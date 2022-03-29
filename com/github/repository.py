import requests, math

class Github:
    def __init__(self, reponame, user_gh, token_gh):
        self.url      = 'https://api.github.com/repos/'+reponame
        self.user_gh  = user_gh
        self.token_gh = token_gh
        self.reponame = reponame
        
    
    def GetAtributes(self, tipo):
        if tipo == 'forks':
            response       = requests.get(self.url, auth=(self.user_gh,self.token_gh))
            data_json      = response.json()
            self.status    = data_json['forks']
            return self.status
        elif tipo == 'stars':
            response       = requests.get(self.url, auth=(self.user_gh,self.token_gh))
            data_json      = response.json()
            self.status    = data_json['stargazers_count']
            return self.status
        elif tipo == 'issues':
            response       = requests.get(self.url, auth=(self.user_gh,self.token_gh))
            data_json      = response.json()
            self.status    = data_json['open_issues_count']
            return self.status
        elif tipo == 'prc':
            response       = requests.get(self.url+'/pulls?state=all&per_page=100', auth=(self.user_gh,self.token_gh))
            data_json      = response.json()
            if len(data_json) == 0:
                return data_json
            else:
                r_total       = requests.get('https://api.github.com/search/issues?q=repo:'+self.reponame+'%20is:pr%20is:open&per_page=1', auth=(self.user_gh,self.token_gh))
                pr_total      = r_total.json()['total_count']
                return pr_total
        elif tipo == 'pr':
            response       = requests.get(self.url+'/pulls?state=all&per_page=100', auth=(self.user_gh,self.token_gh))
            data_json      = response.json()
            if len(data_json) == 0:
                return data_json
            else:
                r_total       = requests.get('https://api.github.com/search/issues?q=repo:'+self.reponame+'%20is:pr%20is:open&per_page=1', auth=(self.user_gh,self.token_gh))
                pr_total      = r_total.json()['total_count']
                pages         = math.ceil(pr_total/100)
                pr_list       = []
                for n_page in range(1, pages+1):
                    response_last = requests.get(self.url+'/pulls?state=open&per_page=100&&page='+str(n_page), auth=(self.user_gh,self.token_gh))
                    data_last     = response_last.json()
                    for i in range (0, len(data_last)):
                        data = {
                                'total': pr_total, 
                                'pr_id': data_last[i]['number'],
                                'repository': self.reponame,
                                'created_at': data_last[i]['created_at'],
                                'title': data_last[i]['title']
                            }
                        pr_list.append(data)
                return pr_list