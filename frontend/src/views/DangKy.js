import React, { useEffect } from "react";
import { Helmet } from 'react-helmet';
import FormDangKy from "../components/admin/FormDangKy";

const DangKy = () =>{
  return (
    <div>
      <Helmet>
        <title>Đăng ký</title>
      </Helmet>
      <FormDangKy/>
    </div>
  );
}

export default DangKy;
