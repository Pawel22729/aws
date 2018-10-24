resource "aws_s3_bucket" "cf_bucket" {
  bucket 	= "plasak-bucket-cf"
  acl		= "private"
  tags {
    Name 	= "plasak-bucket-cf"
  }
}

resource "aws_cloudfront_distribution" "elb_distribution" {
  origin {
    domain_name = "example-lb-167556520.us-east-1.elb.amazonaws.com"
    origin_id = "pablo-origin-id"
  }

  enabled		= true
  default_root_object 	= "index.html"
  default_cache_behavior {
    allowed_methods	= ["GET", "POST"]
    cached_methods	= ["GET"]
    target_origin_id	= "pablo-origin-id"
    forwarded_values {
      query_string 	= true
      headers 		= ["Origin"]
      cookies {
        forward 	= "none"
      }
    }
    viewer_protocol_policy	= "allow-all"
  }

  restrictions {
    geo_restriction {
      restriction_type	= "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }
}
