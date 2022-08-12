class User:

    def __init__(self, user_email, name, password, current_job_title):
    
     
        self.email = user_email
        self.name = name
        self.title = current_job_title
        self.password = password

    def change_password(self,new_password):
        self.password = new_password

    def change_title(self,new_title):
       
        self.title = new_title

    def get_user_info(self):
        print(f"\n\n{self.name} works as a {self.title} and can be contacted at {self.email}.\n\n")



app_user_one = User("Azmeer@gmail.com","Azmeer","3214","Python_Expert")
app_user_one.get_user_info()
app_user_one.change_title('Python_Coder')
app_user_one.get_user_info()