import React, { useState } from 'react';
import './Home.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { 
  faShield, 
  faUsers, 
  faUser, 
  faFileText, 
  faUpload, 
  faDownload, 
  faCheckCircle, 
  faChevronDown, 
  faChevronUp,
  faArrowRight 
} from '@fortawesome/free-solid-svg-icons';

const Home = ({ onNavigate }) => {
  const [showSteps, setShowSteps] = useState(false);
  const [showFeatures, setShowFeatures] = useState(false);

  const steps = [
    {
      number: "01",
      title: "Upload CSV File",
      description: "Select and upload your AWS IAM CSV export file containing user or group data.",
      icon: faUpload
    },
    {
      number: "02", 
      title: "Process Data",
      description: "Our system analyzes your CSV file and generates comprehensive IAM reports.",
      icon: faFileText
    },
    {
      number: "03",
      title: "Download Report", 
      description: "Get your processed report with detailed insights and recommendations.",
      icon: faDownload
    },
    {
      number: "04",
      title: "Implement Changes",
      description: "Use the insights to optimize your AWS IAM security and access management.",
      icon: faCheckCircle
    }
  ];

  const features = [
    {
      icon: faShield,
      title: "Security Analysis",
      description: "Comprehensive security assessment of your IAM configurations",
      color: "blue"
    },
    {
      icon: faUsers,
      title: "Group Management",
      description: "Streamlined group analysis and optimization recommendations",
      color: "green"
    },
    {
      icon: faUser,
      title: "User Management", 
      description: "Detailed user access reviews and compliance reporting",
      color: "purple"
    },
    {
      icon: faFileText,
      title: "Detailed Reports",
      description: "Export comprehensive reports for audit and compliance purposes",
      color: "orange"
    }
  ];

  return (
    <div className="home-container">
      {/* Hero Section */}
      <div className="hero-section">
        <div className="hero-icon">
          <FontAwesomeIcon icon={faShield} />
        </div>
        
        <h1 className="hero-title">
          AWS IAM Management
          <div className="hero-subtitle">Dashboard</div>
        </h1>
        
        <p className="hero-description">
          Streamline your AWS Identity and Access Management with our advanced CSV processing platform. 
          Analyze, optimize, and secure your IAM configurations with comprehensive reporting and insights.
        </p>
        
        <div className="badge-container">
          <span className="badge badge-blue">✨ Advanced Analytics</span>
          <span className="badge badge-green">🛡️ Security Focused</span>
          <span className="badge badge-purple">📊 Detailed Reports</span>
        </div>
      </div>

      

      {/* Features Section */}
      <div className="card">
        <div className="card-header">
          <h2 className="card-title">Key Features</h2>
          <button 
            className="toggle-button" 
            onClick={() => setShowFeatures(!showFeatures)}
          >
            <span>
              {showFeatures ? 'Hide Details' : 'Show Details'}
            </span>
            <FontAwesomeIcon 
              icon={showFeatures ? faChevronUp : faChevronDown} 
            />
          </button>
        </div>
        
        <div className="features-grid">
          {features.map((feature, index) => (
            <div key={index} className="feature-card">
              <div className="feature-icon">
                <FontAwesomeIcon 
                  icon={feature.icon} 
                  className={`icon-${feature.color}`}
                />
              </div>
              <h3 className="feature-title">{feature.title}</h3>
              {showFeatures && (
                <p className="feature-description fade-in">
                  {feature.description}
                </p>
              )}
            </div>
          ))}
        </div>
      </div>

      {/* How It Works Section */}
      <div className="card">
        <div className="card-header">
          <h2 className="card-title">How It Works</h2>
          <button 
            className="toggle-button" 
            onClick={() => setShowSteps(!showSteps)}
          >
            <span>
              {showSteps ? 'Hide Steps' : 'Show Steps'}
            </span>
            <FontAwesomeIcon 
              icon={showSteps ? faChevronUp : faChevronDown} 
            />
          </button>
        </div>
        
        <div className="steps-grid">
          {steps.map((step, index) => (
            <div key={index} className="step-card">
              <div className="step-number">{step.number}</div>
              <h3 className="step-title">
                <FontAwesomeIcon icon={step.icon} />
                <span>{step.title}</span>
              </h3>
              {showSteps && (
                <p className="step-description fade-in">
                  {step.description}
                </p>
              )}
            </div>
          ))}
        </div>
        
        {showSteps && (
          <div className="security-note fade-in">
            <div className="security-note-content">
              <div className="security-note-icon">
                <FontAwesomeIcon icon={faShield} />
              </div>
              <div>
                <h4 className="security-note-title">Security & Compliance</h4>
                <p className="security-note-text">
                  Our platform follows AWS security best practices and helps you maintain compliance 
                  with industry standards. All data processing is done securely with comprehensive 
                  error handling and validation.
                </p>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Home;