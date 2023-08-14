---
title: "Lake Formation Permissions"
date: 2020-07-09T10:24:25-05:00
weight: 21
draft: false
---

24. Now that we have avoided erroneous data to be written to our data lake, let’s verify the data access permissions in AWS Lake Formation on the successful records so our data analysts can consume the data. 
![png](../../static/images/Picture24.png)

25. Once in Lake Formation click on data lake permissions and filter for the data-analyst permissions.
![png](../../static/images/Picture25.png)

26. As we can observe our data analyst has access only to the pass table and only to certain columns in the table.
![png](../../static/images/Picture26.png)

Now let’s test these permissions for the data-analyst

27. First let’s switch roles to the data-analyst role. Click on the data-owner role at the top right corner of the screen and click on Switch role.
![png](../../static/images/Picture29.png)


28. Enter the Account number provided by your host and the role data-analyst then click on switch role.
![png](../../static/images/Picture30.png)

29. Once logged in search for the Athena service and click on Athena
![png](../../static/images/Picture33.png)

30. In the Athena query editor first we need to setup our query results S3 bucket

    a) click on the edit settings button
    ![png](../../static/images/Athena1.png)

    b) Enter the S3 path to the query results folder: 
    s3://dg-workshop-AWSACCOUNT#/athena-results/
    ![png](../../static/images/Athena2.png)

31. As we can see we have only access to the pass table.

In Athena select the insurancedb database and run the following query:

SELECT * FROM "insurancedb"."pass" limit 10;
![png](../../static/images/Picture34.png)


If we inspect the results, we can notice that our Lake Formation permissions have been applied and we only have access to the granted columns in the table.


</br>


