# Table of contents
1. [Partitioning - Use Case SQL](#Partitioning)
2. [Formating Dates in SQL Server](#DateFormatting)
2. [Year month list between start date and current date](#YearMonthList)

## :point_right:Partitioning - Use Case SQL <a name="Partitioning"></a>

**Given Table:**

![image](https://user-images.githubusercontent.com/41752761/197496993-75b29d66-4ea6-46ab-9956-69ced2d6c31c.png)


**Task:** Find the count of new users for each of the days from the above table.

**Expected Output:**

![image](https://user-images.githubusercontent.com/41752761/197494906-c0ffba98-5a78-4abd-807f-d968844fad45.png)


**Solution:**

![image](https://user-images.githubusercontent.com/41752761/197601983-3cf391b6-55f3-4441-80ca-c65df5568e83.png)


## :point_right:Formatting Dates in SQL Server - Reference Site <a name="DateFormatting"></a>
[Click Here](https://www.mssqltips.com/sqlservertip/2655/format-sql-server-dates-with-format-function/)

## :point_right:Year month list between start date and current date <a name="YearMonthList"></a>
```
DECLARE @StartDate  DATE = '2022-06-01',
        @EndDate    DATE = CAST(YEAR(GETDATE()) AS Varchar(4)) + '-'+ CAST(MONTH(GETDATE()) AS Varchar(2))+'-'+'01';

        
SELECT    DATEPART(MM,TempData.TempMonth + '1,1') AS [Month], TempData.TempYear AS [Year]
FROM    (
            SELECT  DATENAME(MONTH, DATEADD(MONTH, x.number, @StartDate)) AS [TempMonth], DATENAME(YEAR, DATEADD(MONTH, x.number, @StartDate)) AS [TempYear]        
            FROM    master.dbo.spt_values x
            WHERE   x.type = 'P'       
            AND     x.number < DATEDIFF(MONTH, @StartDate, @EndDate)
        )    TempData
```

**Output:**

![image](https://user-images.githubusercontent.com/41752761/198926007-cfdd92d0-9475-4036-a4d7-5a3d20f081f6.png)

