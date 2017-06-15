#!/usr/local/bin/ruby
# encoding: utf-8

require 'cgi'
incDir = "/usr/local/www/honey/Include/"
errStr = "ファイルが見つかりません。"

cgi = CGI.new

honeystr = ""
headStr = <<"EOS"
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
EOS


honeystr += <<"EOS"
<!--
ハニーポット用文字列

EOS

begin
  Dir.glob(incDir + "*.rule") do |rule|
    honeystr += "[#{File.basename(rule)}]\n"
    File.open(rule) do |file|
      file.each_line do |str|
	honeystr += CGI.escapeHTML(str)
      end
    end
    honeystr += "\n"
  end
rescue => e
  puts "Err: #{e}\n"  
end

#末尾にランダム文字列付与
honeystr += "[random]\n"
for i in 1..Random.rand(1000) do
  honeystr+= "wp"
end  

#footer
footStr = ""
footStr += <<"EOS"

-->
</body>
</html>
EOS

puts cgi.header("type" => "text/html", "status" => "200 OK")
puts headStr
puts errStr + "<br>\n"
puts honeystr
puts footStr
