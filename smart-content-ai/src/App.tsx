import React, { useState } from 'react';
import InputForm from './components/InputForm';
import ResultBox from './components/ResultBox';
import styled from 'styled-components';
import { BsGithub, BsLinkedin } from 'react-icons/bs';

const AppContainer = styled.div`
  min-height: 100vh;
  background: linear-gradient(135deg, #0a0f24, #000);
  color: white;
  padding: 20px;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px;
`;

const Title = styled.h1`
  text-align: center;
  margin-bottom: 10px;
  font-size: 60px;
`;

const Description = styled.p`
  text-align: justify;
  width: 90%;
  max-width: 800px;
  font-size: 18px;
  margin-bottom: 40px;
`;

const SocialLinksContainer = styled.div`
  position: absolute;
  top: 20px;
  right: 20px;
  display: flex;
  align-items: center;
  gap: 15px;
`;

const SocialText = styled.a`
  color: white;
  text-decoration: none;
  font-size: 16px;
  transition: color 0.3s ease, transform 0.3s ease;
  
  &:hover {
    color: white;
    transform: scale(1.1);
  }
`;

const IconLink = styled.a`
  color: white;
  font-size: 24px;
  transition: color 0.3s ease, transform 0.3s ease;
  
  &:hover {
    color: white;
    transform: scale(1.2);
  }
`;

const Footer = styled.footer`
  width: 100%;
  padding-top: 16px;
  padding-bottom: 6px;
  text-align: center;
  font-size: 14px;
  color: #999;
  position: relative;
  
  a {
    color: #999;
    text-decoration: none;

    &:hover {
      color: white;
    }
  }
`;

interface ResultData {
  transcription: string;
  dalle_image_url: string;
  titles: string[];
  descriptions: string[];
}

function App() {
  const [result, setResult] = useState<ResultData | null>(null);

  return (
    <AppContainer>
      <SocialLinksContainer>
        <SocialText href="#"></SocialText>
        <IconLink href="https://github.com/victoresende19" target="_blank" rel="noopener noreferrer">
          <BsGithub />
        </IconLink>
        <IconLink href="https://www.linkedin.com/in/victor-resende-508b75196/" target="_blank" rel="noopener noreferrer">
          <BsLinkedin />
        </IconLink>
      </SocialLinksContainer>
      <Title>SmartContent AI</Title>
      <Description>
        Sua plataforma para transformar vídeos do YouTube em conteúdos irresistíveis com títulos criativos, descrições envolventes e thumbnails impactantes!
      </Description>
      <InputForm setResult={setResult} />
      <ResultBox result={result} />
      <Footer>
        <a href="#">&copy; 2024 </a> - Victor Augusto Souza Resende
      </Footer>
    </AppContainer>
  );
}

export default App;
