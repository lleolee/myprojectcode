#!/usr/bin/ruby -w
 
require 'net/smtp'
 
message = <<MESSAGE_END
From: Private Person <me@fromdomain.com>
To: A Test User <test@todomain.com>
Subject: SMTP e-mail test
 
This is a test e-mail message.
MESSAGE_END
 
Net::SMTP.start('localhost') do |smtp|
  smtp.send_message message, 'll_501@163.com', 
                             'll_501@163.com'
end