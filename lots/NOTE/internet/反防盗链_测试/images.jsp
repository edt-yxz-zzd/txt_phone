<%@page contentType="image/jpeg" import="java.io.OutputStream,java.io.InputStream,java.net.URL,java.net.URLConnection" language="java"%>
<%
    try{
        OutputStream os = response.getOutputStream();
        //获取图片路径url=http://www.sohu.com/images/aaa.jpg
        String picPath = request.getQueryString();
        //获取纯路径 http://www.sohu.com/images/aaa.jpg
        picPath = picPath.substring(4,picPath.length());
        //建立请求链接
        URLConnection u = new URL(picPath).openConnection();
        InputStream in = u.getInputStream();
        if (null != in) {
            int len;
            byte[] b = new byte[1024];
            while ((len = in.read(b)) != -1) {
                os.write(b, 0, len);
            }
            os.flush();
            in.close();
        }
        os.close();
        out.clear();
        //将图片内容重写到页面
        out = pageContext.pushBody();
    }catch(Exception e){
        e.printStackTrace();
    }
%>
