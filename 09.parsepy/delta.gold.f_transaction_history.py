from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from datetime import date, timedelta, datetime
# from google.cloud import bigquery
from sqlalchemy import create_engine, types
from sqlalchemy.types import VARCHAR, DATE, FLOAT, INTEGER
from sqlalchemy.dialects.oracle import TIMESTAMP, NCLOB
from pyspark.sql import Window
from pyspark.sql import functions as f
import boto3
import pyspark
from pyspark.sql.functions import current_timestamp,col,lit,struct
import boto3
from pyspark.sql.functions import input_file_name
import sys

print(sys.argv)


spark = SparkSession.builder \
    .appName("Ty") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()
sc = spark.sparkContext

today = datetime.now().date()
spark.conf.set("spark.sql.session.timeZone", "+7")
spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", "false")


dwh_path = 's3://data-bic-lake-zone/serving-zone/EDW/'



W_INTEGRATION_ID = ['TRANSACTION_ID',lit('1')]
W_DATASOURCE_ID = lit('1')
partition_by = ['YEAR','MONTH']
w_batch_id = int(sys.argv[1])


df_source = spark.sql(f"""
select
concat('20',left(case when fs.`date_time` = 'None' then null else fs.`date_time` end,6)) `DATE_WID`
,coalesce(cu.row_wid,0) `CUSTOMER_WID`
,coalesce(ac.row_wid,0) `ACCOUNT_WID`
,coalesce(co.row_wid,0) `COMPANY_WID`
,coalesce(dtt.row_wid,0) `TRANSACTION_TYPE_WID`
,coalesce(ptt.row_wid,0) `PMH_TRANSACTION_TYPE_WID`
,case when fs.`recid` = 'None' then null else fs.`recid` end `TRANSACTION_ID`
,case when fs.`transaction_code` = 'None' then null else fs.`transaction_code` end `TRANSACTION_CODE`
,tt2.`transaction_type` `TRANSACTION_TYPE`
,case when tt.transaction_type = 'None' then null else tt.transaction_type end `PMT_TRANSACTION_TYPE`
,case when tt.third_party_channel = 'None' then null else tt.third_party_channel end `THIRD_PARTY_CHANNEL`
,case when fs.`customer_id` = 'None' then null else fs.`customer_id` end `CUSTOMER_ID`
,case when fs.`account_number` = 'None' then null else fs.`account_number` end `ACCOUNT_NUMBER`
,case when fs.`account_officer` = 'None' then null else fs.`account_officer` end `ACCOUNT_OFFICER`
,case when fs.`product_category` = 'None' then null else fs.`product_category` end `PRODUCT_CATEGORY`
,case when fs.`company_code` = 'None' then null else fs.`company_code` end `COMPANY_CODE`
,case when fs.`curr_no` = 'None' then null else fs.`curr_no` end `CURR_NO`
,case when fs.`currency` = 'None' then null else fs.`currency` end `CURRENCY`
,cast(case when fs.`amount_lcy` = 'None' then null else fs.`amount_lcy` end as numeric(20,10)) `AMOUNT_LCY`
,cast(case when fs.`amount_fcy` = 'None' then null else fs.`amount_fcy` end as numeric(20,10)) `AMOUNT_FCY`
,cast(case when fs.`exchange_rate` = 'None' then null else fs.`exchange_rate` end as numeric(20,10)) `EXCHANGE_RATE`
,case when fs.`override` = 'None' then null else fs.`override` end `OVERRIDE`
,case when fs.`reversal_marker` = 'None' then null else fs.`reversal_marker` end `REVERSAL_MARKER`
,case when fs.`position_type` = 'None' then null else fs.`position_type` end `POSITION_TYPE`
,case when fs.`our_reference` = 'None' then null else fs.`our_reference` end `OUR_REFERENCE`
,case when fs.`their_reference` = 'None' then null else fs.`their_reference` end `THEIR_REFERENCE`
,case when fs.`exposure_date` = 'None' then null else fs.`exposure_date` end `EXPOSURE_DATE`
,case when fs.`currency_market` = 'None' then null else fs.`currency_market` end `CURRENCY_MARKET`
,case when fs.`department_code` = 'None' then null else fs.`department_code` end `DEPARTMENT_CODE`
,case when fs.`trans_reference` = 'None' then null else fs.`trans_reference` end `TRANS_REFERENCE`
,case when fs.`system_id` = 'None' then null else fs.`system_id` end `SYSTEM_ID`
,case when fs.`record_status` = 'None' then null else fs.`record_status` end `RECORD_STATUS`
,case when fs.`crf_type` = 'None' then null else fs.`crf_type` end `CRF_TYPE`
,case when fs.`dealer_desk` = 'None' then null else fs.`dealer_desk` end `DEALER_DESK`
,case when fs.`cheque_number` = 'None' then null else fs.`cheque_number` end `CHEQUE_NUMBER`
,case when fs.`chq_coll_id` = 'None' then null else fs.`chq_coll_id` end `CHQ_COLL_ID`
,case when fs.`chq_type` = 'None' then null else fs.`chq_type` end `CHQ_TYPE`
,case when fs.`contract_bal_id` = 'None' then null else fs.`contract_bal_id` end `CONTRACT_BAL_ID`
,case when fs.`balance_type` = 'None' then null else fs.`balance_type` end `BALANCE_TYPE`
,case when fs.`cycle_forward` = 'None' then null else fs.`cycle_forward` end `CYCLE_FORWARD`
,case when fs.`original_acct` = 'None' then null else fs.`original_acct` end `ORIGINAL_ACCT`
,case when fs.`bank_sort_cde` = 'None' then null else fs.`bank_sort_cde` end `BANK_SORT_CDE`
,case when fs.`pc_applied` = 'None' then null else fs.`pc_applied` end `PC_APPLIED`
,case when fs.`pc_period_end` = 'None' then null else fs.`pc_period_end` end `PC_PERIOD_END`
,case when fs.`tax_data` = 'None' then null else fs.`tax_data` end `TAX_DATA`
,case when fs.`tdgl_details` = 'None' then null else fs.`tdgl_details` end `TDGL_DETAILS`
,case when fs.`mask_print` = 'None' then null else fs.`mask_print` end `MASK_PRINT`
,case when fs.`orig_ccy_market` = 'None' then null else fs.`orig_ccy_market` end `ORIG_CCY_MARKET`
,case when fs.`draft_payee_name` = 'None' then null else fs.`draft_payee_name` end `DRAFT_PAYEE_NAME`
,case when fs.`soft_acctng_dtls` = 'None' then null else fs.`soft_acctng_dtls` end `SOFT_ACCTNG_DTLS`
,case when fs.`stmt_no` = 'None' then null else fs.`stmt_no` end `STMT_NO`
,case when tr.`narrative` = 'None' then null else tr.`narrative` end `NARRATIVE`
,case when tr.`data_capture` = 'None' then null else tr.`data_capture` end `DATA_CAPTURE`
,case when tr.`cheque_ind` = 'None' then null else tr.`cheque_ind` end `CHEQUE_IND`
,case when tr.`mandatory_ref_no` = 'None' then null else tr.`mandatory_ref_no` end `MANDATORY_REF_NO`
,case when tr.`debit_credit_ind` = 'None' then null else tr.`debit_credit_ind` end `DEBIT_CREDIT_IND`
,case when tr.`turnover_charge` = 'None' then null else tr.`turnover_charge` end `TURNOVER_CHARGE`
,case when tr.`swift_narrative` = 'None' then null else tr.`swift_narrative` end `SWIFT_NARRATIVE`
,case when tr.`initiation` = 'None' then null else tr.`initiation` end `INITIATION`
,case when tr.`short_desc` = 'None' then null else tr.`short_desc` end `SHORT_DESC`
,case when tr.`stmt_narr` = 'None' then null else tr.`stmt_narr` end `STMT_NARR`
,case when tr.`stmt_narr_ref` = 'None' then null else tr.`stmt_narr_ref` end `STMT_NARR_REF`
,case when tr.`narr_type` = 'None' then null else tr.`narr_type` end `NARR_TYPE`
,case when tr.`dispo_exempt` = 'None' then null else tr.`dispo_exempt` end `DISPO_EXEMPT`
,case when tr.`co_code` = 'None' then null else tr.`co_code` end `CO_CODE`
,case when tr.`dept_code` = 'None' then null else tr.`dept_code` end `DEPT_CODE`
,case when fs.`inputter` = 'None' then null else fs.`inputter` end `INPUTTER`
,case when fs.`authoriser` = 'None' then null else fs.`authoriser` end `AUTHORISER`
,case when fs.`pos_exp_date` = 'None' then null else fs.`pos_exp_date` end `POS_EXP_DATE`
,case when fs.`accounting_date` = 'None' then null else fs.`accounting_date` end `ACCOUNTING_DATE`
,case when fs.`booking_date` = 'None' then null else fs.`booking_date` end `BOOKING_DATE`
,case when fs.`processing_date` = 'None' then null else fs.`processing_date` end `PROCESSING_DATE`
,to_timestamp(left(case when fs.`date_time` = 'None' then null else fs.`date_time` end,6),'yyMMdd') `DATE_TIME`
,YEAR(to_timestamp(left(case when fs.`date_time` = 'None' then null else fs.`date_time` end,6),'yyMMdd')) `YEAR`
,MONTH(to_timestamp(left(case when fs.`date_time` = 'None' then null else fs.`date_time` end,6),'yyMMdd')) `MONTH`
from delta.SILVER.FHO1_STMT_ENTRY fs
left join delta.bronze.FBNK_TRANSACTION tr on fs.`transaction_code` = tr.recid
left join delta.GOLD.D_CUSTOMER cu on fs.`customer_id` = cu.customer_no
left join delta.GOLD.D_ACCOUNT ac on fs.`account_number` = ac.account_number
left join delta.GOLD.D_COMPANY co on fs.`company_code` = co.company_code
left join delta.SILVER.PMH_TRANSACTION_TYPE tt ON (fs.`our_reference` = tt.ft_reference_code)
left join (
   SELECT DISTINCT
     split(recid, ';')[0] our_reference
   , transaction_type
   FROM
     delta.SILVER.FHO1_FUNDS_TRANSFER000
)  tt2 ON (fs.our_reference = tt2.our_reference)
left join delta.GOLD.D_TRANSACTION_TYPE dtt on tt2.transaction_type = dtt.transaction_type_code
left join delta.GOLD.D_PMH_TRANSACTION_TYPE ptt on tt.transaction_type = Ptt.transaction_code
WHERE 1 = 1
and fs.w_batch_id = {w_batch_id}
and fs.`date_time` <> 'None'
--or concat('20',left(case when fs.`date_time` = 'None' then null else fs.`date_time` end,6)) >= '20240501'
--and coalesce(ptt.row_wid,0) <> 0
""")


df_source_01 = df_source\
.withColumn('W_INTEGRATION_ID', concat_ws('~', *W_INTEGRATION_ID)) \
.withColumn('W_DELETE_FLG',lit(0))\
.withColumn('W_INSERT_DATE',current_timestamp())\
.withColumn('W_UPDATE_DATE',current_timestamp())\
.withColumn('W_DATASOURCE_ID',W_DATASOURCE_ID)\
.withColumn('W_BATCH_ID',lit(w_batch_id))



df_source_02 = df_source_01.dropDuplicates(['W_INTEGRATION_ID'])
df_source_02.createTempView('source_tmp')

cl_list = df_source_02.columns
cl_list.remove('W_INSERT_DATE')
str_merge= ','.join([f"tgt.`{i}` = src.`{i}`" for i in cl_list])

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('data-bic-lake-zone')
list = []
for file in my_bucket.objects.filter(Prefix="serving-zone/EDW/GOLD/F_TRANSACTION_HISTORY"):
    file_path = file.key
    list.append('s3://data-bic-lake-zone/'+file_path)
if list:

  spark.sql(f'''
  MERGE INTO delta.`{dwh_path}GOLD/F_TRANSACTION_HISTORY` tgt
  USING source_tmp src
  ON tgt.W_INTEGRATION_ID = src.W_INTEGRATION_ID
  WHEN MATCHED THEN
    UPDATE SET
      {str_merge}
  WHEN NOT MATCHED
    THEN INSERT *
  ''')
else:
  df_source_02.write.format('delta').option("overwriteSchema", "True").partitionBy(partition_by).mode('overwrite').save(f"{dwh_path}GOLD/F_TRANSACTION_HISTORY")


print("--------------ETL_SUCCESS----------------------")
