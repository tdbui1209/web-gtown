import React from "react";
import Header from "../components/admin/header";
import FormQuanLyLoaiSanPham from "../components/admin/FormQuanLyLoaiSanPham";
import TableLoaiSanPham from "../components/admin/TableLoaiSanPham";

const QuanLyLoaiSanPham = () =>{
  return(
    <div>
      <Header/>
      <FormQuanLyLoaiSanPham/>
      <TableLoaiSanPham/>
    </div>
  );
}

export default QuanLyLoaiSanPham;