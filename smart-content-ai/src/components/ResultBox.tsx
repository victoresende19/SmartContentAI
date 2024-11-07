import React from 'react';
import styled from 'styled-components';

const ResultContainer = styled.div`
  background-color: #1E212D;
  color: white;
  padding: 20px;
  margin: 20px auto;
  width: 80%;
  border-radius: 10px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  text-align: justify;
`;

const ImageContainer = styled.div`
  display: flex;
  justify-content: center; /* Centraliza a imagem horizontalmente */
  margin-top: 20px;
`;

const Image = styled.img`
  max-width: 100%;
  border-radius: 5px;
`;

interface ResultProps {
    result: {
        transcription: string;
        dalle_image_url: string;
        titles: string[];
        descriptions: string[];
    } | null;
}

const ResultBox: React.FC<ResultProps> = ({ result }) => {
    if (!result) return null;

    return (
        <ResultContainer>
            <h1>Títulos</h1>
            <ul>
                {result.titles.map((title, index) => (
                    <li key={index}>{title}</li>
                ))}
            </ul>

            <h1>Descrições</h1>
            <ul>
                {result.descriptions.map((desc, index) => (
                    <li key={index}>{desc}</li>
                ))}
            </ul>

            <h1>Imagem gerada</h1>
            <ImageContainer>
                <Image src={result.dalle_image_url} alt="Generated thumbnail" />
            </ImageContainer>
        </ResultContainer>
    );
};

export default ResultBox;
