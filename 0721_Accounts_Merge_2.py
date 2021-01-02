class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        name_to_email_groups = defaultdict(list)
        
        for account in accounts:
            name = account[0]
            emails = account[1:]
            
            if name not in name_to_email_groups:
                name_to_email_groups[name].append(set(emails))
            else:
                email_groups = name_to_email_groups[name]
                found_groups = []
                for idx, group in enumerate(email_groups):
                    if any([email in group for email in emails]):
                        found_groups.append(idx)

                if len(found_groups) == 0:
                    email_groups.append(set(emails))
                else:
                    found_groups.sort()
                    base_group_id = found_groups[0]

                    email_groups[base_group_id].update(emails)

                    for group_id in reversed(found_groups[1:]):
                        email_groups[base_group_id].update(email_groups[group_id])
                        del email_groups[group_id]
        
        new_accounts = []
        for name, email_groups in name_to_email_groups.items():
            for email_group in email_groups:
                new_accounts.append([name] + sorted(email_group))
                
        return new_accounts
