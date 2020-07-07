https://blog.csdn.net/tTU1EvLDeLFq5btqiK/article/details/80089070
主流浏览器图片反防盗链方法总结
    [fail][meta]
        <meta name='referrer' content="never">
        ...
    [success][proxy]
        http://www.thinkphp.cn/code/4826.html
            http://api.hahacn.com/other/getimg2?url=http://img2.kanimg.kankan.com//gallery2/block/2018/07/25/ef23babccf56483b42156a1501229cbc.jpg
            http://api.hahacn.com/other/getimg?host=img01.sogoucdn.com&url=aHR0cDovL2ltZzAxLnNvZ291Y2RuLmNvbS9uZXQvYS8wNC9saW5rP2FwcGlkPTEwMDE0MDAxOSZ1cmw9aHR0cCUzQSUyRiUyRnBpYzcucWl5aXBpYy5jb20lMkZpbWFnZSUyRjIwMTcwNjAxJTJGMTMlMkYxYyUyRmFfMTAwMDI0ODIwX21fNjAxX201XzE5NV8yNjAuanBn
                #base64 的地址

https://blog.csdn.net/quuqu/article/details/52965691?utm_source=blogxgwz6
破解防盗链的图片的一些方法总结
    使用php来做一个下载生成，只需要两行代码即可完成
    [fail]

https://blog.csdn.net/qq_27113373/article/details/51188480
破解图片防盗链方法
    images.jsp
    [fail]

https://blog.csdn.net/iteye_5904/article/details/82091724
绕过图片防盗链的方法
    [fail]
    * iframe
        <script>
            window.sc =
                "<img src='http://<image_url>.jpg?"
                +Math.random()
                +"'>"
                ;
        </script>
        <iframe
            id="imiframe"
            src="javascript:parent.sc"
            style="border:none; overflow: hidden;"
            scrolling="no"
            frameborder="0"
            onload="javascript:var x=document.getElementById('imiframe').contentWindow.document.images[0];this.width=x.width+10;this.height=x.height+10;"
            >
        </iframe>

    * curl
        showpic.php
        http://<your-domain-name>/showpic.php?url=<image_url>


