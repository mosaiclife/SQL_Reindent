# -*- coding: utf-8 -*-

"""
SELECT
FROM
WHERE
JOIN
CASE


UNION
WITH
"""

data = """
SELECT T1.BASE_YM
   , T1.DEBIT_CDIT_DIV
   , T1.THACPL_CURR_AMT
   , T2.FNST_STEP1_CD
   , CASE WHEN T2.FNST_STEP1_CD = 'BS' THEN '10'      -- 대차대조표
          ELSE '20'                                   -- 손익계산서
     END             AS RPRT_DIV
   , T2.FNST_STEP_DIV
   , T2.FNST_STEP2_CD
   , T2.FNST_STEP3_CD
   , T2.FNST_STEP4_CD
   , T2.FNST_STEP5_CD
   , CASE WHEN T1.DEBIT_CDIT_DIV = 'S' THEN DECODE(T2.FNST_STEP_DIV, '1', 1, '2', -1, 0) * T1.THACPL_CURR_AMT
          ELSE 0
     END                          AS DEBIT_AMT
   , CASE WHEN T1.DEBIT_CDIT_DIV = 'H' THEN DECODE(T2.FNST_STEP_DIV, '1', 1, '2', -1, 0) * T1.THACPL_CURR_AMT
          ELSE 0
     END                          AS CDIT_AMT
FROM DW..DFI_F_GELED_ANALS T1         -- 총계정원장분석
JOIN DW..DCM_D_FNST_STEP T2           -- 재무제표단계
  ON T1.GL_ACC_NO BETWEEN T2.DLMT_GL_ACC_NO AND T2.ULMT_GL_ACC_NO
WHERE 1 = 1
 AND T1.BASE_YM BETWEEN '#$ETL_STR_MM#' AND '#$ETL_END_MM#'
"""


sql = data.split()

print sql
print len(sql)

# for i in range(len(sql)):
    # print sql[i]
    