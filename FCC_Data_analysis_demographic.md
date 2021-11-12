# Demographic Data Analyzer Walkthrough

### Import module and read data


```python
import pandas as pd
```


```python
df = pd.read_csv("adult.data.csv")
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>workclass</th>
      <th>fnlwgt</th>
      <th>education</th>
      <th>education-num</th>
      <th>marital-status</th>
      <th>occupation</th>
      <th>relationship</th>
      <th>race</th>
      <th>sex</th>
      <th>capital-gain</th>
      <th>capital-loss</th>
      <th>hours-per-week</th>
      <th>native-country</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>39</td>
      <td>State-gov</td>
      <td>77516</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Never-married</td>
      <td>Adm-clerical</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Male</td>
      <td>2174</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50</td>
      <td>Self-emp-not-inc</td>
      <td>83311</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>2</th>
      <td>38</td>
      <td>Private</td>
      <td>215646</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Divorced</td>
      <td>Handlers-cleaners</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>3</th>
      <td>53</td>
      <td>Private</td>
      <td>234721</td>
      <td>11th</td>
      <td>7</td>
      <td>Married-civ-spouse</td>
      <td>Handlers-cleaners</td>
      <td>Husband</td>
      <td>Black</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>4</th>
      <td>28</td>
      <td>Private</td>
      <td>338409</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Wife</td>
      <td>Black</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>Cuba</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>32556</th>
      <td>27</td>
      <td>Private</td>
      <td>257302</td>
      <td>Assoc-acdm</td>
      <td>12</td>
      <td>Married-civ-spouse</td>
      <td>Tech-support</td>
      <td>Wife</td>
      <td>White</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>38</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>32557</th>
      <td>40</td>
      <td>Private</td>
      <td>154374</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Married-civ-spouse</td>
      <td>Machine-op-inspct</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>32558</th>
      <td>58</td>
      <td>Private</td>
      <td>151910</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Widowed</td>
      <td>Adm-clerical</td>
      <td>Unmarried</td>
      <td>White</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>32559</th>
      <td>22</td>
      <td>Private</td>
      <td>201490</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Never-married</td>
      <td>Adm-clerical</td>
      <td>Own-child</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>20</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>32560</th>
      <td>52</td>
      <td>Self-emp-inc</td>
      <td>287927</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Wife</td>
      <td>White</td>
      <td>Female</td>
      <td>15024</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
  </tbody>
</table>
<p>32561 rows × 15 columns</p>
</div>



### Race Count


```python
race_count = pd.Series(df["race"]).value_counts()
```


```python
race_count
```




    White                 27816
    Black                  3124
    Asian-Pac-Islander     1039
    Amer-Indian-Eskimo      311
    Other                   271
    Name: race, dtype: int64



### Avarage Age Men


```python
avarage_age_men = (df[df["sex"] == "Male"])["age"].mean()
```


```python
avarage_age_men
```




    39.4



### Percentage With Bachelor Degree


```python
percentage_bachelor = ((df[df["education"] == "Bachelors").count()/df.count())[0]*100
```


```python
percentage_bachelor
```




    16.44605509658794



### Percantage with and without higher education that make more than 50k

#### Single out those with education = "Bachelors" or "Masters" or "Doctorate"


```python
higher_education = df[((df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate"))]
higher_education
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>workclass</th>
      <th>fnlwgt</th>
      <th>education</th>
      <th>education-num</th>
      <th>marital-status</th>
      <th>occupation</th>
      <th>relationship</th>
      <th>race</th>
      <th>sex</th>
      <th>capital-gain</th>
      <th>capital-loss</th>
      <th>hours-per-week</th>
      <th>native-country</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>39</td>
      <td>State-gov</td>
      <td>77516</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Never-married</td>
      <td>Adm-clerical</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Male</td>
      <td>2174</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50</td>
      <td>Self-emp-not-inc</td>
      <td>83311</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>4</th>
      <td>28</td>
      <td>Private</td>
      <td>338409</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Wife</td>
      <td>Black</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>Cuba</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>5</th>
      <td>37</td>
      <td>Private</td>
      <td>284582</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Wife</td>
      <td>White</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>8</th>
      <td>31</td>
      <td>Private</td>
      <td>45781</td>
      <td>Masters</td>
      <td>14</td>
      <td>Never-married</td>
      <td>Prof-specialty</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Female</td>
      <td>14084</td>
      <td>0</td>
      <td>50</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>32538</th>
      <td>38</td>
      <td>Private</td>
      <td>139180</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Divorced</td>
      <td>Prof-specialty</td>
      <td>Unmarried</td>
      <td>Black</td>
      <td>Female</td>
      <td>15020</td>
      <td>0</td>
      <td>45</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>32539</th>
      <td>71</td>
      <td>?</td>
      <td>287372</td>
      <td>Doctorate</td>
      <td>16</td>
      <td>Married-civ-spouse</td>
      <td>?</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>32544</th>
      <td>31</td>
      <td>Private</td>
      <td>199655</td>
      <td>Masters</td>
      <td>14</td>
      <td>Divorced</td>
      <td>Other-service</td>
      <td>Not-in-family</td>
      <td>Other</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>30</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>32553</th>
      <td>32</td>
      <td>Private</td>
      <td>116138</td>
      <td>Masters</td>
      <td>14</td>
      <td>Never-married</td>
      <td>Tech-support</td>
      <td>Not-in-family</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>Taiwan</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>32554</th>
      <td>53</td>
      <td>Private</td>
      <td>321865</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
  </tbody>
</table>
<p>7491 rows × 15 columns</p>
</div>



#### Percentage with higher education AND salary >50K


```python
higher_education_rich = ((higher_education[higher_education["salary"] == ">50K"]).count()/higher_education.count())[0]*100
higher_education_rich
```




    46.535843011613935



#### Single out those with NOT education = "Bachelors" or "Masters" or "Doctorate"


```python
lower_education = df[~((df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate"))]
lower_education
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>workclass</th>
      <th>fnlwgt</th>
      <th>education</th>
      <th>education-num</th>
      <th>marital-status</th>
      <th>occupation</th>
      <th>relationship</th>
      <th>race</th>
      <th>sex</th>
      <th>capital-gain</th>
      <th>capital-loss</th>
      <th>hours-per-week</th>
      <th>native-country</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>38</td>
      <td>Private</td>
      <td>215646</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Divorced</td>
      <td>Handlers-cleaners</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>3</th>
      <td>53</td>
      <td>Private</td>
      <td>234721</td>
      <td>11th</td>
      <td>7</td>
      <td>Married-civ-spouse</td>
      <td>Handlers-cleaners</td>
      <td>Husband</td>
      <td>Black</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>6</th>
      <td>49</td>
      <td>Private</td>
      <td>160187</td>
      <td>9th</td>
      <td>5</td>
      <td>Married-spouse-absent</td>
      <td>Other-service</td>
      <td>Not-in-family</td>
      <td>Black</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>16</td>
      <td>Jamaica</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>7</th>
      <td>52</td>
      <td>Self-emp-not-inc</td>
      <td>209642</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>45</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>10</th>
      <td>37</td>
      <td>Private</td>
      <td>280464</td>
      <td>Some-college</td>
      <td>10</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>Black</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>80</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>32556</th>
      <td>27</td>
      <td>Private</td>
      <td>257302</td>
      <td>Assoc-acdm</td>
      <td>12</td>
      <td>Married-civ-spouse</td>
      <td>Tech-support</td>
      <td>Wife</td>
      <td>White</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>38</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>32557</th>
      <td>40</td>
      <td>Private</td>
      <td>154374</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Married-civ-spouse</td>
      <td>Machine-op-inspct</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>32558</th>
      <td>58</td>
      <td>Private</td>
      <td>151910</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Widowed</td>
      <td>Adm-clerical</td>
      <td>Unmarried</td>
      <td>White</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>32559</th>
      <td>22</td>
      <td>Private</td>
      <td>201490</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Never-married</td>
      <td>Adm-clerical</td>
      <td>Own-child</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>20</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>32560</th>
      <td>52</td>
      <td>Self-emp-inc</td>
      <td>287927</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Wife</td>
      <td>White</td>
      <td>Female</td>
      <td>15024</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
  </tbody>
</table>
<p>25070 rows × 15 columns</p>
</div>



#### Percentage with lower education AND salary >50K


```python
lower_education_rich = ((lower_education[lower_education["salary"] == ">50K"]).count()/lower_education.count())[0]*100
lower_education_rich
```




    17.3713601914639



### Minimum numbers of hours a person works per week


```python
df["hours-per-week"].min()
```




    1



#### Who works only 1 hour per week


```python
min_workers = df[df["hours-per-week"] == df["hours-per-week"].min()]
# Equal to: df[df["hours-per-week"] == 1]
min_workers
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>workclass</th>
      <th>fnlwgt</th>
      <th>education</th>
      <th>education-num</th>
      <th>marital-status</th>
      <th>occupation</th>
      <th>relationship</th>
      <th>race</th>
      <th>sex</th>
      <th>capital-gain</th>
      <th>capital-loss</th>
      <th>hours-per-week</th>
      <th>native-country</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>189</th>
      <td>58</td>
      <td>State-gov</td>
      <td>109567</td>
      <td>Doctorate</td>
      <td>16</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>1036</th>
      <td>66</td>
      <td>Self-emp-inc</td>
      <td>150726</td>
      <td>9th</td>
      <td>5</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>1409</td>
      <td>0</td>
      <td>1</td>
      <td>?</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>1262</th>
      <td>69</td>
      <td>?</td>
      <td>195779</td>
      <td>Assoc-voc</td>
      <td>11</td>
      <td>Widowed</td>
      <td>?</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>5590</th>
      <td>78</td>
      <td>?</td>
      <td>363134</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Widowed</td>
      <td>?</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>5632</th>
      <td>45</td>
      <td>?</td>
      <td>189564</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-civ-spouse</td>
      <td>?</td>
      <td>Wife</td>
      <td>White</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>5766</th>
      <td>62</td>
      <td>?</td>
      <td>97231</td>
      <td>Some-college</td>
      <td>10</td>
      <td>Married-civ-spouse</td>
      <td>?</td>
      <td>Wife</td>
      <td>White</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>5808</th>
      <td>76</td>
      <td>?</td>
      <td>211574</td>
      <td>10th</td>
      <td>6</td>
      <td>Married-civ-spouse</td>
      <td>?</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>8447</th>
      <td>67</td>
      <td>?</td>
      <td>244122</td>
      <td>Assoc-voc</td>
      <td>11</td>
      <td>Widowed</td>
      <td>?</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>9147</th>
      <td>75</td>
      <td>?</td>
      <td>260543</td>
      <td>10th</td>
      <td>6</td>
      <td>Widowed</td>
      <td>?</td>
      <td>Other-relative</td>
      <td>Asian-Pac-Islander</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>China</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>11451</th>
      <td>27</td>
      <td>Private</td>
      <td>147951</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Never-married</td>
      <td>Machine-op-inspct</td>
      <td>Other-relative</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>19337</th>
      <td>72</td>
      <td>?</td>
      <td>76860</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Married-civ-spouse</td>
      <td>?</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>19750</th>
      <td>23</td>
      <td>Private</td>
      <td>72887</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Never-married</td>
      <td>Craft-repair</td>
      <td>Own-child</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>Vietnam</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>20072</th>
      <td>65</td>
      <td>?</td>
      <td>76043</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Married-civ-spouse</td>
      <td>?</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>20909</th>
      <td>77</td>
      <td>Self-emp-not-inc</td>
      <td>71676</td>
      <td>Some-college</td>
      <td>10</td>
      <td>Widowed</td>
      <td>Adm-clerical</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Female</td>
      <td>0</td>
      <td>1944</td>
      <td>1</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>22960</th>
      <td>21</td>
      <td>Private</td>
      <td>184135</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Never-married</td>
      <td>Machine-op-inspct</td>
      <td>Own-child</td>
      <td>Black</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>23536</th>
      <td>69</td>
      <td>?</td>
      <td>320280</td>
      <td>Some-college</td>
      <td>10</td>
      <td>Never-married</td>
      <td>?</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Male</td>
      <td>1848</td>
      <td>0</td>
      <td>1</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>24284</th>
      <td>57</td>
      <td>Self-emp-not-inc</td>
      <td>56480</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>25078</th>
      <td>74</td>
      <td>Private</td>
      <td>260669</td>
      <td>10th</td>
      <td>6</td>
      <td>Divorced</td>
      <td>Other-service</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>29752</th>
      <td>69</td>
      <td>?</td>
      <td>117525</td>
      <td>Assoc-acdm</td>
      <td>12</td>
      <td>Divorced</td>
      <td>?</td>
      <td>Unmarried</td>
      <td>White</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>32525</th>
      <td>81</td>
      <td>?</td>
      <td>120478</td>
      <td>Assoc-voc</td>
      <td>11</td>
      <td>Divorced</td>
      <td>?</td>
      <td>Unmarried</td>
      <td>White</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>?</td>
      <td>&lt;=50K</td>
    </tr>
  </tbody>
</table>
</div>



#### How many are they


```python
num_min_workers = (df[df["hours-per-week"] == df["hours-per-week"].min()]).count()[0]
num_min_workers
```




    20



#### Percentage with salary >50K


```python
rich_percentage = (min_workers[min_workers["salary"] == ">50K"].count()/num_min_workers*100)[0]
rich_percentage
```




    10.0



### What country have highest percentage of people earning >50K


```python
countries = df["native-country"].value_counts().index
countries
```




    Index(['United-States', 'Mexico', '?', 'Philippines', 'Germany', 'Canada',
           'Puerto-Rico', 'El-Salvador', 'India', 'Cuba', 'England', 'Jamaica',
           'South', 'China', 'Italy', 'Dominican-Republic', 'Vietnam', 'Guatemala',
           'Japan', 'Poland', 'Columbia', 'Taiwan', 'Haiti', 'Iran', 'Portugal',
           'Nicaragua', 'Peru', 'France', 'Greece', 'Ecuador', 'Ireland', 'Hong',
           'Cambodia', 'Trinadad&Tobago', 'Laos', 'Thailand', 'Yugoslavia',
           'Outlying-US(Guam-USVI-etc)', 'Honduras', 'Hungary', 'Scotland',
           'Holand-Netherlands'],
          dtype='object')




```python
high_earners = (df[df["salary"] == ">50K"])
high_earners
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>workclass</th>
      <th>fnlwgt</th>
      <th>education</th>
      <th>education-num</th>
      <th>marital-status</th>
      <th>occupation</th>
      <th>relationship</th>
      <th>race</th>
      <th>sex</th>
      <th>capital-gain</th>
      <th>capital-loss</th>
      <th>hours-per-week</th>
      <th>native-country</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>52</td>
      <td>Self-emp-not-inc</td>
      <td>209642</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>45</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>8</th>
      <td>31</td>
      <td>Private</td>
      <td>45781</td>
      <td>Masters</td>
      <td>14</td>
      <td>Never-married</td>
      <td>Prof-specialty</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Female</td>
      <td>14084</td>
      <td>0</td>
      <td>50</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>9</th>
      <td>42</td>
      <td>Private</td>
      <td>159449</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>5178</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>10</th>
      <td>37</td>
      <td>Private</td>
      <td>280464</td>
      <td>Some-college</td>
      <td>10</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>Black</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>80</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>11</th>
      <td>30</td>
      <td>State-gov</td>
      <td>141297</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>32539</th>
      <td>71</td>
      <td>?</td>
      <td>287372</td>
      <td>Doctorate</td>
      <td>16</td>
      <td>Married-civ-spouse</td>
      <td>?</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>32545</th>
      <td>39</td>
      <td>Local-gov</td>
      <td>111499</td>
      <td>Assoc-acdm</td>
      <td>12</td>
      <td>Married-civ-spouse</td>
      <td>Adm-clerical</td>
      <td>Wife</td>
      <td>White</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>20</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>32554</th>
      <td>53</td>
      <td>Private</td>
      <td>321865</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>32557</th>
      <td>40</td>
      <td>Private</td>
      <td>154374</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Married-civ-spouse</td>
      <td>Machine-op-inspct</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>32560</th>
      <td>52</td>
      <td>Self-emp-inc</td>
      <td>287927</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Wife</td>
      <td>White</td>
      <td>Female</td>
      <td>15024</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&gt;50K</td>
    </tr>
  </tbody>
</table>
<p>7841 rows × 15 columns</p>
</div>




```python
highest_perc = 0
highest_country = ""
for country in countries:
    high_earners_in_country = high_earners[high_earners["native-country"] == country]
    perc_high_earners = round(((high_earners_in_country.count()/(df[df["native-country"] == country]).count())[0])*100, 1)
    if perc_high_earners > highest_perc:
        highest_perc = perc_high_earners
        highest_country = country
print(highest_perc, highest_country)

```

    41.9 Iran



```python
highest_earning_country_percentage = (((df[df["salary"] == ">50K"])["native-country"].value_counts())[0]/df[df["native-country"] == highest_earning_country].count())[0]*100
```




    24.583476174151524



### Identify the most popular occupation for those who earn >50K in India


```python
ppl_india = df[df["native-country"] == "India"]
ppl_india
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>workclass</th>
      <th>fnlwgt</th>
      <th>education</th>
      <th>education-num</th>
      <th>marital-status</th>
      <th>occupation</th>
      <th>relationship</th>
      <th>race</th>
      <th>sex</th>
      <th>capital-gain</th>
      <th>capital-loss</th>
      <th>hours-per-week</th>
      <th>native-country</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11</th>
      <td>30</td>
      <td>State-gov</td>
      <td>141297</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>892</th>
      <td>28</td>
      <td>Private</td>
      <td>164170</td>
      <td>Assoc-voc</td>
      <td>11</td>
      <td>Married-civ-spouse</td>
      <td>Adm-clerical</td>
      <td>Wife</td>
      <td>Asian-Pac-Islander</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>968</th>
      <td>48</td>
      <td>Private</td>
      <td>164966</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>1029</th>
      <td>48</td>
      <td>Self-emp-inc</td>
      <td>138370</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-spouse-absent</td>
      <td>Sales</td>
      <td>Not-in-family</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>50</td>
      <td>India</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>1095</th>
      <td>22</td>
      <td>Self-emp-not-inc</td>
      <td>361280</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Never-married</td>
      <td>Prof-specialty</td>
      <td>Own-child</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>20</td>
      <td>India</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>30152</th>
      <td>48</td>
      <td>Private</td>
      <td>119471</td>
      <td>Doctorate</td>
      <td>16</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>30833</th>
      <td>25</td>
      <td>Private</td>
      <td>110978</td>
      <td>Assoc-acdm</td>
      <td>12</td>
      <td>Married-civ-spouse</td>
      <td>Adm-clerical</td>
      <td>Wife</td>
      <td>Asian-Pac-Islander</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>37</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>30871</th>
      <td>26</td>
      <td>Private</td>
      <td>160261</td>
      <td>Masters</td>
      <td>14</td>
      <td>Never-married</td>
      <td>Prof-specialty</td>
      <td>Not-in-family</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>20</td>
      <td>India</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>31327</th>
      <td>38</td>
      <td>State-gov</td>
      <td>125499</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>7688</td>
      <td>0</td>
      <td>60</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>31357</th>
      <td>23</td>
      <td>Private</td>
      <td>143003</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>1887</td>
      <td>50</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 15 columns</p>
</div>




```python
ppl_w_high_salary_india = ppl_india[ppl_india["salary"] == ">50K"]
ppl_w_high_salary_india
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>workclass</th>
      <th>fnlwgt</th>
      <th>education</th>
      <th>education-num</th>
      <th>marital-status</th>
      <th>occupation</th>
      <th>relationship</th>
      <th>race</th>
      <th>sex</th>
      <th>capital-gain</th>
      <th>capital-loss</th>
      <th>hours-per-week</th>
      <th>native-country</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11</th>
      <td>30</td>
      <td>State-gov</td>
      <td>141297</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>968</th>
      <td>48</td>
      <td>Private</td>
      <td>164966</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>1327</th>
      <td>52</td>
      <td>Private</td>
      <td>168381</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Widowed</td>
      <td>Other-service</td>
      <td>Unmarried</td>
      <td>Asian-Pac-Islander</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>7258</th>
      <td>42</td>
      <td>State-gov</td>
      <td>102343</td>
      <td>Prof-school</td>
      <td>15</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>72</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>7285</th>
      <td>54</td>
      <td>State-gov</td>
      <td>93449</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>8124</th>
      <td>36</td>
      <td>Private</td>
      <td>172104</td>
      <td>Prof-school</td>
      <td>15</td>
      <td>Never-married</td>
      <td>Prof-specialty</td>
      <td>Not-in-family</td>
      <td>Other</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>9939</th>
      <td>43</td>
      <td>Federal-gov</td>
      <td>325706</td>
      <td>Prof-school</td>
      <td>15</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>50</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>10590</th>
      <td>35</td>
      <td>Private</td>
      <td>98283</td>
      <td>Prof-school</td>
      <td>15</td>
      <td>Never-married</td>
      <td>Prof-specialty</td>
      <td>Not-in-family</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>10661</th>
      <td>59</td>
      <td>Private</td>
      <td>122283</td>
      <td>Prof-school</td>
      <td>15</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>99999</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>10736</th>
      <td>30</td>
      <td>Private</td>
      <td>243190</td>
      <td>Prof-school</td>
      <td>15</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>20</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>11260</th>
      <td>54</td>
      <td>Private</td>
      <td>225599</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>7298</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>11384</th>
      <td>34</td>
      <td>Private</td>
      <td>98283</td>
      <td>Prof-school</td>
      <td>15</td>
      <td>Never-married</td>
      <td>Tech-support</td>
      <td>Not-in-family</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>1564</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>13422</th>
      <td>53</td>
      <td>Private</td>
      <td>366957</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>99999</td>
      <td>0</td>
      <td>50</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>13551</th>
      <td>40</td>
      <td>Private</td>
      <td>220977</td>
      <td>Doctorate</td>
      <td>16</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>3103</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>13862</th>
      <td>45</td>
      <td>Private</td>
      <td>209912</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>16017</th>
      <td>41</td>
      <td>Private</td>
      <td>207578</td>
      <td>Assoc-acdm</td>
      <td>12</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>Black</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>50</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>16778</th>
      <td>43</td>
      <td>Private</td>
      <td>242968</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>16923</th>
      <td>41</td>
      <td>Private</td>
      <td>143003</td>
      <td>Assoc-voc</td>
      <td>11</td>
      <td>Married-civ-spouse</td>
      <td>Other-service</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>7298</td>
      <td>0</td>
      <td>60</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>17259</th>
      <td>57</td>
      <td>Self-emp-inc</td>
      <td>123053</td>
      <td>Prof-school</td>
      <td>15</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>15024</td>
      <td>0</td>
      <td>50</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>17834</th>
      <td>29</td>
      <td>Self-emp-not-inc</td>
      <td>341672</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Married-spouse-absent</td>
      <td>Transport-moving</td>
      <td>Other-relative</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>1564</td>
      <td>50</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>20417</th>
      <td>42</td>
      <td>Self-emp-inc</td>
      <td>23510</td>
      <td>Masters</td>
      <td>14</td>
      <td>Divorced</td>
      <td>Exec-managerial</td>
      <td>Unmarried</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>2201</td>
      <td>60</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>20465</th>
      <td>39</td>
      <td>Private</td>
      <td>198654</td>
      <td>Prof-school</td>
      <td>15</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>2415</td>
      <td>67</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>21128</th>
      <td>30</td>
      <td>Private</td>
      <td>122889</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>50</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>23474</th>
      <td>55</td>
      <td>State-gov</td>
      <td>120781</td>
      <td>Doctorate</td>
      <td>16</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>24154</th>
      <td>46</td>
      <td>Private</td>
      <td>229737</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Sales</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>50</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>25739</th>
      <td>35</td>
      <td>Self-emp-inc</td>
      <td>79586</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>26305</th>
      <td>27</td>
      <td>Private</td>
      <td>207352</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Tech-support</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>26356</th>
      <td>34</td>
      <td>Private</td>
      <td>99872</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>3103</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>27670</th>
      <td>61</td>
      <td>Private</td>
      <td>80896</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>45</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>28264</th>
      <td>51</td>
      <td>Self-emp-not-inc</td>
      <td>120781</td>
      <td>Prof-school</td>
      <td>15</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Other</td>
      <td>Male</td>
      <td>99999</td>
      <td>0</td>
      <td>70</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>28433</th>
      <td>42</td>
      <td>Private</td>
      <td>198341</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>1902</td>
      <td>55</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>28452</th>
      <td>53</td>
      <td>Private</td>
      <td>70387</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>4386</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>28557</th>
      <td>34</td>
      <td>Private</td>
      <td>165737</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>43</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>28651</th>
      <td>45</td>
      <td>Self-emp-not-inc</td>
      <td>216402</td>
      <td>Prof-school</td>
      <td>15</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>50</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>28798</th>
      <td>30</td>
      <td>Self-emp-not-inc</td>
      <td>116666</td>
      <td>Masters</td>
      <td>14</td>
      <td>Divorced</td>
      <td>Prof-specialty</td>
      <td>Not-in-family</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>50</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>30111</th>
      <td>41</td>
      <td>Federal-gov</td>
      <td>219155</td>
      <td>Prof-school</td>
      <td>15</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>50</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>30152</th>
      <td>48</td>
      <td>Private</td>
      <td>119471</td>
      <td>Doctorate</td>
      <td>16</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>30833</th>
      <td>25</td>
      <td>Private</td>
      <td>110978</td>
      <td>Assoc-acdm</td>
      <td>12</td>
      <td>Married-civ-spouse</td>
      <td>Adm-clerical</td>
      <td>Wife</td>
      <td>Asian-Pac-Islander</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>37</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>31327</th>
      <td>38</td>
      <td>State-gov</td>
      <td>125499</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>7688</td>
      <td>0</td>
      <td>60</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
    <tr>
      <th>31357</th>
      <td>23</td>
      <td>Private</td>
      <td>143003</td>
      <td>Masters</td>
      <td>14</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Husband</td>
      <td>Asian-Pac-Islander</td>
      <td>Male</td>
      <td>0</td>
      <td>1887</td>
      <td>50</td>
      <td>India</td>
      <td>&gt;50K</td>
    </tr>
  </tbody>
</table>
</div>




```python
ranking_occ = ppl_w_high_salary_india["occupation"].value_counts()
ranking_occ
```




    Prof-specialty      25
    Exec-managerial      8
    Other-service        2
    Tech-support         2
    Transport-moving     1
    Sales                1
    Adm-clerical         1
    Name: occupation, dtype: int64




```python
highest_ranking_occ = ranking_occ.index[0]
highest_ranking_occ
```




    'Prof-specialty'


