import React, { useState } from 'react';
import axios from 'axios';
import styled from 'styled-components';
import CircularProgress from '@mui/material/CircularProgress';

const FormWrapper = styled.div`
  background-color: rgba(255, 255, 255, 0.1); /* Caixa opaca */
  backdrop-filter: blur(10px); /* Efeito de desfoque no fundo */
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  max-width: 600px;
  width: 80%;
  margin: 0 auto;
`;

const FormContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 14px;
`;

const Input = styled.input`
  width: 50%;
  padding: 15px;
  margin: 10px 0;
  border-radius: 5px;
  border: 1px solid #ccc;
  height: 30px;
`;

const Button = styled.button`
  padding: 10px 20px;
  border: none;
  background-color: white;
  color: #1E1F27;
  border-radius: 5px;
  cursor: pointer;
  position: relative;
  font-size: 16px;

  &:hover {
    background-color: #4a4c59;
    color: white;
  }

  &:disabled {
    background-color: #4a4c59;
    cursor: not-allowed;
    color: white;
  }
`;

const ButtonContent = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
`;

interface InputFormProps {
    setResult: (result: any) => void;
}

const InputForm: React.FC<InputFormProps> = ({ setResult }) => {
    const [videoUrl, setVideoUrl] = useState<string>('');
    const [loading, setLoading] = useState<boolean>(false);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        try {
          const response = await axios.post('https://smartcontentai.onrender.com/generate-video-details/', {
                video_url: videoUrl,
            });
            setResult(response.data);
        } catch (error) {
            console.error('Error fetching data:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <FormWrapper>
            <FormContainer>
                <h2>Insira o link de um vídeo do YouTube para gerar conteúdos dinâmicos</h2>
                <Input
                    type="text"
                    placeholder="Insira um link do YouTube..."
                    value={videoUrl}
                    onChange={(e: React.ChangeEvent<HTMLInputElement>) => setVideoUrl(e.target.value)}
                />
                <Button onClick={handleSubmit} disabled={loading}>
                    <ButtonContent>
                        {loading && <CircularProgress size={20} style={{ color: 'white' }} />}
                        Gerar conteúdo ✨
                    </ButtonContent>
                </Button>
            </FormContainer>
        </FormWrapper>
    );
};

export default InputForm;
