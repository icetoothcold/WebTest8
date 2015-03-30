#coding:utf8
__author__ = 'Lyan'



def str_sql_time(time):
    if len(time)==1:

        s="and (to_char(r.firstoccurrence,'yyyy-mm-dd hh24:mi:ss') between '%s' and '%s')" % (time[0],time[1])
        print s
    else :

        s_time=''
        for t in time:
            if t==time[0]:
                s_time1="(to_char(r.firstoccurrence,'yyyy-mm-dd hh24:mi:ss') between '%s' and '%s')" % (t[0],t[1])
                #print s_time1

            else:
                s_time1="OR(to_char(r.firstoccurrence,'yyyy-mm-dd hh24:mi:ss') between '%s' and '%s')" % (t[0],t[1])
            s_time+=s_time1
        s="and ("+s_time+")"
    #print s
    return s



def str_sql_ip(ip):
    if ip:
        IP="and r.nodealias='%s'" % ip
    else:
        IP=''
    print IP
    return IP


def strSQL(s,IP):
    strSQL = """
    select distinct r.serverserial   as"事件序号",
    r.treventid       as "事件编码",
    e.evntname        as "事件名称",
    r.node            as "机器名称",
    r.nodealias       as "物理IP",
    r.trownername     as "事件属主",
    r.trobjectname    as "事件对象",
    r.firstoccurrence as "首次发生时间",
    r.tally           as "报警次数",
    r.summary         as "事件信息",
    r.manager         as "事件源",
    e.whodo           as "操作人",
    r.TRSPEVNTKEY    as "特定事件编号"
    from reporter.reporter_status r, monitor.event e, monitor.machine m,CMDB.mv_configurationitem mc
    where r.treventid = e.evntid
    and r.manager not in('netiq@VMW4038-NETIQ-TRCON')
    and m.sdid = r.trmachineid
    and r.severity >=3
    and r.trstatus !=8
    and r.treventid not like '13%'
    and r.treventid not like '12%'
    and r.treventid not like '14%'
    and m.status ='使用中'
    and m.searchcode = mc.searchcode
    and mc.cicode6 in ('S2','S3','S4')
    and mc.cicode5='生产'
    and mc.status='ʹ使用中'
    and mc.category='逻辑服务器单元'
    """ + s +IP
    return strSQL
def strSQL_machine(s,IP):
    strSQL_machine="""select distinct r.serverserial   as"事件序号",
    r.treventid       as "事件编码",
    e.evntname        as "事件名称",
    r.node            as "机器名称",
    r.nodealias       as "物理IP",
    r.trownername     as "事件属主",
    r.trobjectname    as "事件对象",
    r.firstoccurrence as "首次发生时间",
    r.tally           as "报警次数",
    r.summary         as "事件信息",
    r.manager         as "事件源",
    e.whodo           as "操作人",
    r.TRSPEVNTKEY    as "特定事件编号"
    from reporter.reporter_status r, monitor.event e
    where r.treventid = e.evntid
    and r.manager not in('netiq@VMW4038-NETIQ-TRCON')
    and r.severity >=3
    and r.trstatus !=8
    and r.treventid not like '13%'
    and r.treventid not like '12%'
    and r.treventid not like '14%'
    and r.manager not in('netiq@VMW4038-NETIQ-TRCON')
    and r.treventid in ('0500010162','0500020079','0500040020','0500050022','0500090001')
    """ + s +IP
    return strSQL_machine

def sql_str(time):

    ip=''
    s=str_sql_time(time)
    IP=str_sql_ip(ip)
    print strSQL(s,IP)
    print strSQL_machine(s,IP)

if __name__ == '__main__':
    time=[('2015-02-14 00:00:00','2015-02-15 23:59:59'),('2015-02-16 00:00:00','2015-02-17 23:59:59'),('2015-02-18 00:00:00','2015-02-19 23:59:59')]
    sql_str()






