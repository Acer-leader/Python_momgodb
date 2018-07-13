# 数据挖掘
- 使用 Python 和 IPython Notebook 

        pip install ipython[all] 
        # 安装 IPython 
        
        ipython notebook
        #启动notebook
- 亲和性分析示例
        
        
 select u.Name,su.Name,sc.Score from user as u left join (select  UserId,sum(Score) as sc from  Score 
 group by userid) sc on sc.userid = u.id`  
 left join (select sco.subjectid,sco.score>=60 as '及格' and sco.score<60 as '不及格' from score as sco  group by subjectid) sco on sco.subjectid = su.id
 
 