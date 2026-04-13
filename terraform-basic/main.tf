# EC2 instance create examples for learning 
resource "aws_instance" "this1" {
  ami = "ami-0861f4e788f5069dd"
  instance_type = "t2.micro"
  key_name = "mount.pem"
  security_groups = ["sg-0b491f46461318532"]
  subnet_id = "subnet-004c0b5d1a93e8916"
  tags = {
    Name = "Instance_terrfaorm"
  }
}

resource "aws_instance" "this2" {
  ami = "ami-0861f4e788f5069dd"
  instance_type = "t2.micro"
  key_name = "mount.pem"
  security_groups = ["sg-0b491f46461318532"]
  subnet_id = "subnet-004c0b5d1a93e8916"
  tags = {
    Name = "Instance_terrfaorm_2"
  }
}