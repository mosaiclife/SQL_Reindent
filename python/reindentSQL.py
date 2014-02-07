# -*- coding: utf-8 -*-

from Tree import Tree

CLAUSES = ['SELECT', 'FROM', 'WHERE']

data = """
SELECT SUBSTR(T2.YM_END_DT,1,6)                    AS BASE_YM        -- 기준년월    
     , T1.MKT_ORG_CD                               AS MKT_ORG_CD     -- 영업조직코드
     , T1.CRCLT_PATH_CD                            AS CRCLT_PATH_CD  -- 유통경로코드
     , T1.MTRL_NO                                  AS MTRL_NO        -- 자재번호    
     , T1.CURR_CD                                  AS CURR_CD        -- 통화코드    
     , T1.UNIT                                     AS UNIT           -- 단위        
     , CAST(T1.BSPR             AS NUMERIC(25,2))  AS BSPR           -- 기준가      
  FROM DW..DSD_B_PRDC_BSPR  T1                         -- 제품별기준가
  INNER JOIN (
       SELECT DISTINCT
              CASE WHEN SUBSTR(T1.YM_END_DT, 1, 6) = TO_CHAR(CURRENT_DATE - 1, 'YYYYMM')
                        THEN TO_CHAR(CURRENT_DATE - 1, 'YYYYMMDD')
                   ELSE T1.YM_END_DT
              END          AS YM_END_DT
         FROM DW..DCM_D_DT  T1
        WHERE T1.BASE_DT BETWEEN '#$ETL_STR_MM#'||'01' AND TO_CHAR(LAST_DAY(TO_DATE('#$ETL_END_MM#'||'01', 'YYYYMMDD')), 'YYYYMMDD')
          AND T1.BASE_DT <= TO_CHAR(CURRENT_DATE, 'YYYYMMDD')
       )  T2
    ON T2.YM_END_DT BETWEEN T1.EFFC_ST_DT AND T1.EFFC_FNS_DT
;
"""

data = """
SELECT  a
    ,   b
FROM    T1
"""

class SQLTree(Tree):

    def __init__(self, data, lchild = None, rchild = None):
        Tree.__init__(self, data)
        self.isLeft = 0
        self.isRight = 0
    
    def insert(self, data):
        if self.lchild is None:
                self.lchild = SQLTree(data)
        else:
            self.lchild.insert(data)



# root = SQLTree('')
# root.insert('SELECT')
# root.insert('a')
# root.insert(',b')
# root.insert(',c')
# root.insert(',d')
# root.insert('FROM')
# root.insert('T1')
# root.preorderTraverse(root)

data = ['SELECT', 'a', ',b', ',c', 'FROM', 'T1']
print data
