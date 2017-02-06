#  
# 描述：  
#   发送快递数据到datasystem使用http  
# 输入：  
#   data   - 组装后的expess的数据  
# 输出：  
#   datasystem返回的状态信息  
#  
def self.senddata(url,data)  
  url  = url + data  
  begin  
    Net::HTTP.version_1_2   # 设定对象的运作方式  
    if ($logger != nil)  
      $logger.info("链接地址参数:#{URI.escape(url)},文件名：#{__FILE__},第 #{__LINE__} 行")  
      $logger.info("传入data参数:#{data.to_json},文件名：#{__FILE__},第 #{__LINE__} 行")  
    end  
    ret_data = Net::HTTP.get(URI.parse(URI.escape(url)))  
  rescue =>exception  
    $logger.error("传递url地址为#{url}，错误!#{exception.to_s},文件名：#{__FILE__},第 #{__LINE__} 行")  
    return nil  
  end  
  return ret_data  
end  
  
  
#  
# 描述：  
#   发送快递数据到datasystem,使用https  
# 输入：  
#   data   - 组装后的expess的数据  
# 输出：  
#   datasystem返回的状态信息  
#  
def self.senddatassl(url,data)  
  url  = url + data  
  $logger.info(url)  
  begin  
    uri = URI.parse(URI.escape(url))  
    http = Net::HTTP.new(uri.host, uri.port)  
    http.use_ssl = true  
      
    if ($logger != nil)  
      $logger.info("链接地址参数:#{URI.escape(url)},文件名：#{__FILE__},第 #{__LINE__} 行")  
      $logger.info("传入data参数:#{data.to_json},文件名：#{__FILE__},第 #{__LINE__} 行")  
    end  
    request = Net::HTTP::Get.new(uri.request_uri)  
      
    response = http.request(request)  
  rescue =>exception  
    $logger.error("传递url地址为#{url}，错误!#{exception.to_s},文件名：#{__FILE__},第 #{__LINE__} 行")  
    return nil  
  end  
  return response.body  
end  
