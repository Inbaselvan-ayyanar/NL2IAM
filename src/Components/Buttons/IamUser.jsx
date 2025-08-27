import React from 'react';
import { useNavigate } from 'react-router-dom';
import './IamUser.css';

const IamUser = () => {
  const navigate = useNavigate();

  return (
    <button className='iamuser-btn' onClick={() => navigate('/iam/user')}>
      IAM User
    </button>
  );
};

export default IamUser;
