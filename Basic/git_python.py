import sh
git = sh.git.bake(_cwd='C:\TestCode\Git_Test\Basic-Web-Development')
print(git.status()) 
# checkout and track a remote branch
#print( git.checkout('-b', 'somebranch'))
# add a file
print(git.add('simple.txt')) 
# commit
print(git.commit(m='Added simple.txt file')) 
# now we are one commit ahead
print(git.status()) 
# pull
#print(git.remotes.origin.pull())
# push
#print(git.remotes.origin.push())
#git config --global http.sslVerify false
git.pull()

# import shutil
# import git
# shutil.copytree("","")
# repo = git.Repo( 'C:\TestCode\Git_Test\Basic-Web-Development' )
# print(repo.git.status()) 
# # checkout and track a remote branch
# #print(repo.git.checkout( 'origin/somebranch', b='somebranch' )) 
# # add a file
# print(repo.git.add( 'simple.txt' ))
# print(repo.git.add( 'simple.txt' ))
# print(repo.git.status())  
# # commit
# print(repo.git.commit( m='Added simple.txt file' )) 
# # now we are one commit ahead
# print(repo.git.status()) 
# # pull
# print(repo.remotes.origin.pull())
# # push
# print(repo.remotes.origin.push())