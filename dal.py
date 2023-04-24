import crypt, os, spwd
import datetime 

class dao:
    def __init__(self) -> None:
        pass

    def authenticate(username, password) -> bool:
        user=spwd.getspnam(username)
        if(crypt.crypt(password, user.sp_pwdp)):
            return True
        return False

    def getUserData(self,path):
        dir = []
        file = []
        if(self.logged):
            for data in os.listdir(path):
                path = f'{path}/{data}'
                size = os.path.getsize(path)
                time = os.path.getmtime(path)
                time_str = datetime.datetime.timestamp(time).strftime('%Y-%m-%d %H:%M:%S')
                path = f'{path}{data}'
                if (os.path.isdir(path)):
                    dir.append(data, time_str, path)
                if (os.path.isfile(path)):
                    file.append(data, time_str, path)
            return(dir, file)
        return []