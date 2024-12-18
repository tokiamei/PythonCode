# 排序

1. `sort_index`：按行或列索引进行排序，按照索引进行排序,注意与reindex()重建索引进行区分

   ```python
   #Series
   s1 = pd.Series(np.arange(4),index=list('dbca'))
   s1
   d    0
   b    1
   c    2
   a    3
   dtype: int32
   
   s1.sort_index() #默认升序
   a    3
   b    1
   c    2
   d    0
   dtype: int32
       
   s1.sort_index(ascending=False) #参数ascending=False降序
   d    0
   c    2
   b    1
   a    3
   dtype: int32
   
   #DataFrmme
   pd1=pd.DataFrame(np.arange(12).reshape(4,3),index=list('bdca'),columns=list('BCa'))pd1
   	B	C	A
   b	0	1	2
   d	3	4	5
   c	6	7	8
   a	9	10	11
   
   #按行排序
   pd1.sort_index()
   	B	C	A
   a	9	10	11
   b	0	1	2
   c	6	7	8
   d	3	4	5
   
   #按列排序，需要知道轴,axis=1或axis='columns'
   pd1.sort_index(axis=1)
   	A	B	C
   b	2	0	1
   d	5	3	4
   c	8	6	7
   a	11	9	10
   #同样如果需要指定降序，需要设置参数ascending=False
   ```

2. `sort_values`：按值进行排序

   ```python
   #Series
   s2 = pd.Series([5,6,np.nan,1,-1])
   s2
   0    5.0
   1    6.0
   2    NaN
   3    1.0
   4   -1.0
   dtype: float64
   
   s2.sort_values() #根据值的大小进行排序,当有缺失值时，会默认排到最后
   4   -1.0
   3    1.0
   0    5.0
   1    6.0
   2    NaN
   dtype: float64
   
   #DataFrame 当我们对dataframe进行值的排序的时候，需要使用参数by
   pd2 = pd.DataFrame({'a':[3,7,9,0],'b':[1,-1,4,8],'c':[0,6,-3,2]})
   pd2
   	a	b	c
   0	3	1	0
   1	7	-1	6
   2	9	4	-3
   3	0	8	2
   
   pd2.sort_values(by='b') #指定b列进行排序
   	a	b	c
   1	7	-1	6
   0	3	1	0
   2	9	4	-3
   3	0	8	2
   #也可以进行多列排序,传递一个列名的列表
   pd2.sort_values(by=['a','c'])
   	a	b	c
   3	0	8	2
   0	3	1	0
   1	7	-1	6
   2	9	4	-3
   #同样我们也可以根据参数ascending=False来进行降序
   pd2.sort_values(by=['a','c'],ascending=False)
   	a	b	c
   2	9	4	-3
   1	7	-1	6
   0	3	1	0
   3	0	8	2
   ```

3. 