def copyfile():
    old_file=input('请输入需要备份的文件名')
    file_list=old_file.split('.')
    new_file=file_list[0]+'_备份.'+file_list[1]
    old_f=open(old_file,'r')
    new_f=open(new_file,'w')
    content=old_f.read()
    new_f.write(content)
    old_f.close()
    new_f.close()
    pass
copyfile()