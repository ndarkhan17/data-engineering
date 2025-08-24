terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.49.2"
    }
  }
}

provider "google" {
  # Configuration options
  credentials = "./keys/terraform-demo-470008-eefd27a592f9.json"
  project     = "terraform-demo-470008"
  region      = "europe-west1"
}


resource "google_storage_bucket" "demo-bucket" {
  name          = "terraform-demo-470008-terra-bucket"
  location      = "EU"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}