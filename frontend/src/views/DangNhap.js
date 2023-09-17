import React, { useEffect } from "react";
import { Helmet } from 'react-helmet';
import FormDangNhap from "../components/admin/FormDangNhap";

const DangNhap = () =>{
  useEffect(() => {
    function handleScreenSizeChange() {
      const screenWidth = window.innerWidth;
      if (screenWidth <= 1021) {
        document.getElementById("sign_in_right_side").style.display = "none";
        document.getElementById("sign_in_left_side").classList.remove("col-md-4");
        document.getElementById("sign_in_left_side").classList.add("col-md-7");
      } else {
        // Show sign_in_right_side and reset sign_in_left_side
        document.getElementById("sign_in_right_side").style.display = "block";
        document.getElementById("sign_in_left_side").classList.remove("col-md-7");
        document.getElementById("sign_in_left_side").classList.add("col-md-4");
      }
    }    

    // Thêm sự kiện resize khi component được mount
    window.addEventListener("resize", handleScreenSizeChange);

    // Xóa sự kiện khi component bị unmount
    return () => {
      window.removeEventListener("resize", handleScreenSizeChange);
    };
  }, []); // [] đảm bảo useEffect chỉ chạy một lần khi component được mount

  return (
    <div>
      <Helmet>
        <title>Đăng nhập</title>
      </Helmet>
      <FormDangNhap/>
    </div>
  );
}

export default DangNhap;
