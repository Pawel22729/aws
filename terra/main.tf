provider "aws" {
  access_key = "${var.access_key}"
  secret_key = "${var.secret_key}"
  region     = "${var.region}"
}

resource "aws_elb" "example-lb" {
  name = "example-lb"
  availability_zones = ["us-east-1a"]
  security_groups = ["${var.sec_gr}"]

  listener {
    instance_port = 80
    instance_protocol = "http"
    lb_port = 80
    lb_protocol = "http"
  }

  health_check {
    healthy_threshold = 2
    unhealthy_threshold = 2
    timeout = 3
    target = "HTTP:80/index.html"
    interval = 10
  }

  instances = ["${aws_instance.example.*.id}"]
  
}

resource "aws_instance" "example" {
  count 	= 1
  ami           = "${var.ami_id}"
  instance_type = "t2.micro"
  availability_zone = "us-east-1a"
  vpc_security_group_ids = "${var.sec_gr}"
  user_data = "${file("user-data.sh")}"
}

module "cloudFront" {
  source = "./cloud_front_module"
}
