<html>
<head>
<title>y.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6a8759;}
.s3 { color: #808080;}
.s4 { color: #6897bb;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
y.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">selenium </span><span class="s0">import </span><span class="s1">webdriver </span><span class="s0">as </span><span class="s1">selenium_wd</span>
<span class="s0">from </span><span class="s1">selenium.webdriver.chrome.options </span><span class="s0">import </span><span class="s1">Options</span>
<span class="s0">from </span><span class="s1">selenium.webdriver.chrome.service </span><span class="s0">import </span><span class="s1">Service</span>
<span class="s0">from </span><span class="s1">selenium.webdriver.common.by </span><span class="s0">import </span><span class="s1">By</span>
<span class="s0">from </span><span class="s1">selenium.webdriver.support </span><span class="s0">import </span><span class="s1">expected_conditions </span><span class="s0">as </span><span class="s1">EC</span>
<span class="s0">from </span><span class="s1">selenium.webdriver.support.ui </span><span class="s0">import </span><span class="s1">WebDriverWait</span>
<span class="s0">from </span><span class="s1">time </span><span class="s0">import </span><span class="s1">sleep</span>

<span class="s1">S = Service(</span><span class="s2">r&quot;C:/text/chromedriver&quot;</span><span class="s1">)</span>
<span class="s1">chrome_options = Options()</span>

<span class="s1">driver = selenium_wd.Chrome(service=S</span><span class="s0">, </span><span class="s1">options=chrome_options)</span>
<span class="s1">driver.get(</span><span class="s2">&quot;https://travelata.ru&quot;</span><span class="s1">)</span>
<span class="s3"># &quot;btn btnOrange btnFlat js-popup-close&quot;</span>

<span class="s1">marketing_banner_locator = (By.XPATH</span><span class="s0">, </span><span class="s2">&quot;//div[@class=</span><span class="s0">\&quot;</span><span class="s2">btn btnOrange btnFlat js-popup-close</span><span class="s0">\&quot;</span><span class="s2">]&quot;</span><span class="s1">)</span>
<span class="s1">market_banner = WebDriverWait(driver</span><span class="s0">, </span><span class="s4">10</span><span class="s1">).until(</span>
    <span class="s1">EC.presence_of_element_located(marketing_banner_locator)</span>
<span class="s1">)</span>
<span class="s1">market_banner.click()</span>

<span class="s1">destination_locator = (By.NAME</span><span class="s0">, </span><span class="s2">&quot;destination&quot;</span><span class="s1">)</span>
<span class="s1">destination = WebDriverWait(driver</span><span class="s0">, </span><span class="s4">10</span><span class="s1">).until(</span>
    <span class="s1">EC.presence_of_element_located(destination_locator)</span>
<span class="s1">)</span>

<span class="s1">destination.clear()</span>
<span class="s1">destination.send_keys(</span><span class="s2">&quot;Самара&quot;</span><span class="s1">)</span>
<span class="s1">sleep(</span><span class="s4">3</span><span class="s1">)</span>

<span class="s1">start_search_locator = (By.ID</span><span class="s0">, </span><span class="s2">&quot;startSearch&quot;</span><span class="s1">)</span>
<span class="s1">start_search = WebDriverWait(driver</span><span class="s0">, </span><span class="s4">10</span><span class="s1">).until(</span>
    <span class="s1">EC.presence_of_element_located(start_search_locator)</span>
<span class="s1">)</span>
<span class="s1">start_search.click()</span>
<span class="s1">sleep(</span><span class="s4">10</span><span class="s1">)</span>
<span class="s1">driver.quit()</span></pre>
</body>
</html>