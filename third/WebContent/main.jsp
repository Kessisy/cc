<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>在此处插入标题</title>
</head>
<%@page import="java.util.*"%>
<body>
<%String username=session.getAttribute("username").toString();
Integer visitCount=(Integer)session.getAttribute("visitCount");
if(visitCount==null){
	visitCount=1;
}else{
	visitCount++;
}
session.setAttribute("visitCount",visitCount);

%>
第<%=visitCount%>访客，您好！<%=username %>欢迎您！<br>
<a href="exit.jsp">退出</a>

</html>