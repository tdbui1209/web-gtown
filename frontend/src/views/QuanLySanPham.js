import React from "react";
//Thay đổi title tương ứng với mỗi Route
import { Helmet } from 'react-helmet';
import Navbar from "../components/admin/Navbar";

const QuanLySanPham = () =>{
  return(
    <div>
      <Helmet>
        <title>Quản lý sản phẩm</title>
      </Helmet>
      <Navbar/>
      <h3>Quản lý sản phẩm</h3>
    </div>
  );
}

export default QuanLySanPham;