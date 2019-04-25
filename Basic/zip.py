import os
import zipfile
import shutil
import git
def git_op(parser_name,dir_path,comment):
    parser_folder_name = parser_name.split('.envision')[0]
    print(parser_folder_name)
    zzip = zipfile.ZipFile(parser_name)
    zzip.extractall()
    dir_path += '\\etc\\devices'
    path1 = os.path.join(dir_path,parser_folder_name)
    print(path1)
    shutil.copytree(path1,'C:\\TestCode\\Git_Test\\Basic-Web-Development\\'+parser_folder_name)
    repo = git.Repo( 'C:\TestCode\Git_Test\Basic-Web-Development' )
    print(repo.git.status()) 
    # add a file
    print(repo.git.add( parser_folder_name))
    print(repo.git.status())  
    # commit
    print(repo.git.commit( m= comment )) 
    # now we are one commit ahead
    print(repo.git.status()) 
    # pull
    print(repo.remotes.origin.pull())
    # push
    print(repo.remotes.origin.push())
    

if __name__ == '__main__':
    os.getcwd()
    os.chdir('C:\CICD\content-qe-tools\content-cdp\output')
    dir_path = os.getcwd()
    parser_name = 'cef.envision'
    comment = 'Parser added'
    git_op(parser_name,dir_path,comment)