<?php
$url = $_GET["url"];
//$url = str_replace("http:/","http://",$url);
$dir = pathinfo($url);
$host = $dir['dirname'];
$refer = $host.'/';

$ch = curl_init($url);
curl_setopt ($ch, CURLOPT_REFERER, $refer);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);//激活可修改页面,Activation can modify the page
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_BINARYTRANSFER, 1);
$data = curl_exec($ch);
curl_close($ch);

$ext = strtolower(substr(strrchr($img,'.'),1,10));
$types = array(
        'gif'=>'image/gif',
        'jpeg'=>'image/jpeg',
        'jpg'=>'image/jpeg',
        'jpe'=>'image/jpeg',
        'png'=>'image/png',
);
$type = $types[$ext] ? $types[$ext] : 'image/jpeg';
header("Content-type: ".$type);
echo $data;
//<img src="http://your-domain-name/showpic.php?url=http://cdn.archdaily.net/wp-content/uploads/2011/06/1309476244-elicium-rai-01-528x351.jpg" />

//---------------------
//作者：iteye_5904
//来源：CSDN
//原文：https://blog.csdn.net/iteye_5904/article/details/82091724
//      绕过图片防盗链的方法
//版权声明：本文为博主原创文章，转载请附上博文链接！
?>

