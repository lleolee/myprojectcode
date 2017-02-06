#  
# ������  
#   ���Ϳ�����ݵ�datasystemʹ��http  
# ���룺  
#   data   - ��װ���expess������  
# �����  
#   datasystem���ص�״̬��Ϣ  
#  
def self.senddata(url,data)  
  url  = url + data  
  begin  
    Net::HTTP.version_1_2   # �趨�����������ʽ  
    if ($logger != nil)  
      $logger.info("���ӵ�ַ����:#{URI.escape(url)},�ļ�����#{__FILE__},�� #{__LINE__} ��")  
      $logger.info("����data����:#{data.to_json},�ļ�����#{__FILE__},�� #{__LINE__} ��")  
    end  
    ret_data = Net::HTTP.get(URI.parse(URI.escape(url)))  
  rescue =>exception  
    $logger.error("����url��ַΪ#{url}������!#{exception.to_s},�ļ�����#{__FILE__},�� #{__LINE__} ��")  
    return nil  
  end  
  return ret_data  
end  
  
  
#  
# ������  
#   ���Ϳ�����ݵ�datasystem,ʹ��https  
# ���룺  
#   data   - ��װ���expess������  
# �����  
#   datasystem���ص�״̬��Ϣ  
#  
def self.senddatassl(url,data)  
  url  = url + data  
  $logger.info(url)  
  begin  
    uri = URI.parse(URI.escape(url))  
    http = Net::HTTP.new(uri.host, uri.port)  
    http.use_ssl = true  
      
    if ($logger != nil)  
      $logger.info("���ӵ�ַ����:#{URI.escape(url)},�ļ�����#{__FILE__},�� #{__LINE__} ��")  
      $logger.info("����data����:#{data.to_json},�ļ�����#{__FILE__},�� #{__LINE__} ��")  
    end  
    request = Net::HTTP::Get.new(uri.request_uri)  
      
    response = http.request(request)  
  rescue =>exception  
    $logger.error("����url��ַΪ#{url}������!#{exception.to_s},�ļ�����#{__FILE__},�� #{__LINE__} ��")  
    return nil  
  end  
  return response.body  
end  
