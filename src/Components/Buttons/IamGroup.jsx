import React from 'react';
import { useNavigate } from 'react-router-dom';
import './IamGroup.css';

const IAMButton = () => {
  const navigate = useNavigate();

  return (
    <button className='iam-btn' onClick={() => navigate('/iam/group')}>
      IAM Group
    </button>
  );
};

export default IAMButton;
