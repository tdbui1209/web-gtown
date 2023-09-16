import React from "react";
//Thay đổi title tương ứng với mỗi Route
import { Helmet } from 'react-helmet';
// import Navbar from "../components/admin/Navbar";

const QuanLyNguoiDung = () =>{
  return(
    <div>
      <Helmet>
        <title>Quản lý người dùng</title>
      </Helmet>
      {/* <Navbar/> */}
      <h3>Quản lý người dùng</h3>
    </div>
  );
}

export default QuanLyNguoiDung;