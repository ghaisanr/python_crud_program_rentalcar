def admin_security(data,username,password):
    for i in range(len(data["username"])):
        if data["username"][i]==username and data["password"][i]==password:
            return True
    


