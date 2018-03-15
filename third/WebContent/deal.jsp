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
<%
String[][] userlist={{"mr","lo"},{"hj","bn"},{"fg","vb"}};
String username=request.getParameter("username");
String password=request.getParameter("password");
boolean flag=false;
for(int i=0;i<userlist.length;i++){
	if(username.equals(userlist[i][0])&&password.equals(userlist[i][1])){
		flag=true;
		break;
	}
}
if(flag){
	session.setAttribute("username", username);	
	response.sendRedirect("main.jsp");
	
}else{
	response.sendRedirect("login.jsp");
}
%>

</body>
</html>