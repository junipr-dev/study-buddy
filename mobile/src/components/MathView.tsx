import React, { useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { WebView } from 'react-native-webview';
import { colors, fontSize } from '../theme';

interface MathViewProps {
  content: string;
}

/**
 * Renders text with LaTeX math expressions using KaTeX in a WebView
 */
export default function MathView({ content }: MathViewProps) {
  const [webviewHeight, setWebviewHeight] = useState<number>(60);

  // Check if content has any LaTeX ($ delimiters)
  const hasLatex = content.includes('$');

  if (!hasLatex) {
    return <Text style={styles.text}>{content}</Text>;
  }

  // HTML template with KaTeX
  const html = `
    <!DOCTYPE html>
    <html>
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
      <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
      <style>
        * {
          margin: 0;
          padding: 0;
          box-sizing: border-box;
        }
        body {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
          font-size: ${fontSize.md}px;
          line-height: 1.6;
          color: ${colors.text};
          background-color: transparent;
          padding: 8px;
        }
        .katex {
          font-size: 1.1em;
        }
        .katex-display {
          margin: 0.5em 0;
        }
      </style>
    </head>
    <body>
      <div id="content">${escapeHtml(content)}</div>
      <script>
        renderMathInElement(document.getElementById('content'), {
          delimiters: [
            {left: '$$', right: '$$', display: true},
            {left: '$', right: '$', display: false},
          ],
          throwOnError: false
        });

        // Send height to React Native
        setTimeout(() => {
          const height = document.body.scrollHeight;
          window.ReactNativeWebView.postMessage(JSON.stringify({ height }));
        }, 100);
      </script>
    </body>
    </html>
  `;

  const handleWebViewMessage = (event: any) => {
    try {
      const message = JSON.parse(event.nativeEvent.data);
      if (message.height) {
        setWebviewHeight(message.height);
      }
    } catch (error) {
      console.error('Failed to parse WebView message:', error);
    }
  };

  return (
    <View style={[styles.container, { minHeight: webviewHeight }]}>
      <WebView
        source={{ html }}
        style={[styles.webview, { height: webviewHeight }]}
        scrollEnabled={false}
        showsVerticalScrollIndicator={false}
        showsHorizontalScrollIndicator={false}
        originWhitelist={['*']}
        javaScriptEnabled
        onMessage={handleWebViewMessage}
      />
    </View>
  );
}

function escapeHtml(text: string): string {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

const styles = StyleSheet.create({
  container: {
    minHeight: 60,
  },
  webview: {
    backgroundColor: 'transparent',
    minHeight: 60,
  },
  text: {
    color: colors.text,
    fontSize: fontSize.md,
    lineHeight: fontSize.md * 1.5,
  },
});
