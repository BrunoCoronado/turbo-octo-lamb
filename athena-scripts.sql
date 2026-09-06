--Database creation
CREATE DATABASE turbo_octo_lamb

--Table definition for intentory data
CREATE EXTERNAL TABLE IF NOT EXISTS turbo_octo_lamb.inventory(
    inventoryItemCode BIGINT,
    inventoryItemId INT,
    inventoryItemDescription STRING,
    initialInventory DECIMAL(11,4),
    mov DECIMAL(11,4),
    value DECIMAL(11,4)
)
--How to parse and interpret each line on csv file
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
   'separatorChar' = ',',
   'quoteChar'     = '"',
   'escapeChar'    = '\\'
)
LOCATION 's3://turbo-octo-lamb-mock-data-113008552223-us-east-1-an/inventory/'
TBLPROPERTIES ('skip.header.line.count'='1');

--Table definition for purchases data
CREATE EXTERNAL TABLE IF NOT EXISTS turbo_octo_lamb.purchases(
    itemPurchaseId INT,
    businessDate STRING,
    itemPurchaseReferenceNumber INT,
    itemPurchaseComment STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
   'separatorChar' = ',',
   'quoteChar'     = '"',
   'escapeChar'    = '\\'
)
LOCATION 's3://turbo-octo-lamb-mock-data-113008552223-us-east-1-an/purchases/'
TBLPROPERTIES ('skip.header.line.count'='1');

ALTER TABLE turbo_octo_lamb.purchases 
SET TBLPROPERTIES ('use.null.for.invalid.data' = 'true');

--Table definition for sales data
CREATE EXTERNAL TABLE IF NOT EXISTS turbo_octo_lamb.sales(
    depositId INT,
    depositTime STRING,
    businessDate STRING,
    salesAreaName STRING,
    voucherNumber STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
   'separatorChar' = ',',
   'quoteChar'     = '"',
   'escapeChar'    = '\\'
)
LOCATION 's3://turbo-octo-lamb-mock-data-113008552223-us-east-1-an/sales/'
TBLPROPERTIES ('skip.header.line.count'='1');

--Get all inventory movements query
SELECT 
    inventoryItemCode,
    inventoryItemId,
    inventoryItemDescription,
    initialInventory,
    mov,
    value
FROM turbo_octo_lamb.inventory;

--Get all purchases detailes query
SELECT 
    itemPurchaseId,
    businessDate,
    itemPurchaseReferenceNumber,
    itemPurchaseComment
FROM turbo_octo_lamb.purchases;

--Get all sales deposits query
SELECT 
    depositId,
    depositTime,
    businessDate,
    salesAreaName,
    voucherNumber
FROM turbo_octo_lamb.sales;