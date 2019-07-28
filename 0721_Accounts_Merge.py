class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        def find(a):
            while parent[a] != a:
                a = parent[a]
            return a
        
        
        def union(a, b):
            parent[find(b)] = find(a)
            
            
        email_to_id, id_to_name = {}, {}
        parent = []
        
        id = 0
        for account in accounts:
            name = account[0]
            default_email = account[1]
            
            for email in account[1:]:
                if email not in email_to_id:
                    parent.append(id)
                    email_to_id[email] = id
                    id_to_name[id] = name
                    id += 1
                union(email_to_id[default_email], email_to_id[email])
                    
            
        # print(email_to_id)
        # print(parent)
        root_id_to_emails = collections.defaultdict(list)
        
        for email, id in email_to_id.items():
            root_id_to_emails[find(id)].append(email)
            
        ans = []
        for id, emails in root_id_to_emails.items():
            ans.append([id_to_name[id]] + sorted(emails))
        return ans
