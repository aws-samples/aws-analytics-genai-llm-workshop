---
title : "Data Quality"
weight : 10
---

#### Section Overview

In this section, we will create a data quality Glue job that will inspect our data against 56 data quality rules 

These rules will:

    1)	Ensure that we have no records with null values 
    
    2)	Ensure strings match specific values 
  
    3)	Ensure we have a range for column lengths 

    4)	Ensure integer values are within a specific range 
  
  If the record passes the data quality checks it will be immediately outputed for querying by business analyst from the pass table in the glue data catalog.

  If the record fail's the data quality checks it will be outputed in the fail table of the glue data catalog so data owners can investigate these records and adjust them in the source systems. 


</br></br>

