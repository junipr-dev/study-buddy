import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  ActivityIndicator,
  ScrollView,
  Modal,
} from 'react-native';
import { useAuthStore } from '../store/authStore';
import { useQuizStore } from '../store/quizStore';
import { colors, spacing, fontSize } from '../theme';
import MathView from '../components/MathView';

export default function QuizScreen() {
  const { user, logout } = useAuthStore();
  const {
    currentQuestion,
    feedback,
    isLoading,
    error,
    fetchNextQuestion,
    submitAnswer,
    clearFeedback,
  } = useQuizStore();

  const [answer, setAnswer] = useState('');

  useEffect(() => {
    if (!currentQuestion && !feedback) {
      fetchNextQuestion();
    }
  }, []);

  const handleSubmit = async () => {
    if (!answer.trim()) return;
    await submitAnswer(answer);
    setAnswer('');
  };

  const handleContinue = () => {
    clearFeedback();
    if (!currentQuestion) {
      fetchNextQuestion();
    }
  };

  const handleLogout = async () => {
    await logout();
  };

  return (
    <View style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.title}>Study Buddy</Text>
        <View style={styles.headerRight}>
          <Text style={styles.userName}>{user?.first_name}</Text>
          <TouchableOpacity onPress={handleLogout}>
            <Text style={styles.logoutText}>Logout</Text>
          </TouchableOpacity>
        </View>
      </View>

      <ScrollView style={styles.content} contentContainerStyle={styles.contentContainer}>
        {error && (
          <View style={styles.errorBox}>
            <Text style={styles.errorText}>{error}</Text>
          </View>
        )}

        {isLoading && !currentQuestion ? (
          <View style={styles.loadingContainer}>
            <ActivityIndicator size="large" color={colors.primary} />
            <Text style={styles.loadingText}>Loading question...</Text>
          </View>
        ) : currentQuestion ? (
          <View style={styles.questionCard}>
            <Text style={styles.skillName}>{currentQuestion.skill_name}</Text>
            <View style={styles.difficultyBadge}>
              <Text style={styles.difficultyText}>
                Level {currentQuestion.difficulty}
              </Text>
            </View>

            <View style={styles.questionContainer}>
              <MathView content={currentQuestion.question} />
            </View>

            <View style={styles.answerSection}>
              <Text style={styles.label}>Your Answer</Text>
              <TextInput
                style={styles.input}
                value={answer}
                onChangeText={setAnswer}
                placeholder="Type your answer..."
                placeholderTextColor={colors.textMuted}
                keyboardType="default"
                autoCapitalize="none"
                onSubmitEditing={handleSubmit}
                editable={!isLoading}
              />
              <TouchableOpacity
                style={[styles.submitButton, isLoading && styles.buttonDisabled]}
                onPress={handleSubmit}
                disabled={isLoading || !answer.trim()}
              >
                {isLoading ? (
                  <ActivityIndicator color={colors.text} />
                ) : (
                  <Text style={styles.submitButtonText}>Submit</Text>
                )}
              </TouchableOpacity>
            </View>
          </View>
        ) : (
          <View style={styles.emptyState}>
            <Text style={styles.emptyText}>No question available</Text>
            <TouchableOpacity style={styles.button} onPress={() => fetchNextQuestion()}>
              <Text style={styles.buttonText}>Load Question</Text>
            </TouchableOpacity>
          </View>
        )}

        <Text style={styles.tip}>
          Tip: The more you practice, the better the adaptive algorithm gets!
        </Text>
      </ScrollView>

      {/* Feedback Modal */}
      <Modal visible={!!feedback} transparent animationType="fade">
        <View style={styles.modalOverlay}>
          <View style={styles.feedbackCard}>
            <View
              style={[
                styles.feedbackHeader,
                feedback?.is_correct ? styles.correctHeader : styles.incorrectHeader,
              ]}
            >
              <Text style={styles.feedbackEmoji}>
                {feedback?.is_correct ? '✓' : '✗'}
              </Text>
              <Text style={styles.feedbackTitle}>
                {feedback?.is_correct ? 'Correct!' : 'Not quite...'}
              </Text>
            </View>

            <View style={styles.feedbackBody}>
              <View style={styles.answerRow}>
                <Text style={styles.answerLabel}>Your answer:</Text>
                <Text style={styles.answerValue}>{feedback?.user_answer}</Text>
              </View>

              {!feedback?.is_correct && (
                <View style={styles.answerRow}>
                  <Text style={styles.answerLabel}>Correct answer:</Text>
                  <Text style={[styles.answerValue, styles.correctAnswer]}>
                    {feedback?.correct_answer}
                  </Text>
                </View>
              )}

              {feedback?.steps && feedback.steps.length > 0 && (
                <View style={styles.stepsContainer}>
                  <Text style={styles.stepsTitle}>Solution Steps:</Text>
                  {feedback.steps.map((step, index) => (
                    <View key={index} style={styles.stepItem}>
                      <MathView content={step} />
                    </View>
                  ))}
                </View>
              )}
            </View>

            <TouchableOpacity style={styles.continueButton} onPress={handleContinue}>
              <Text style={styles.continueButtonText}>Continue</Text>
            </TouchableOpacity>
          </View>
        </View>
      </Modal>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.background,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: spacing.md,
    paddingTop: spacing.xl + spacing.md,
    backgroundColor: colors.surface,
    borderBottomWidth: 1,
    borderBottomColor: colors.border,
  },
  title: {
    fontSize: fontSize.lg,
    fontWeight: 'bold',
    color: colors.text,
  },
  headerRight: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.md,
  },
  userName: {
    color: colors.text,
    fontWeight: '500',
  },
  logoutText: {
    color: colors.textMuted,
    fontSize: fontSize.sm,
  },
  content: {
    flex: 1,
  },
  contentContainer: {
    padding: spacing.md,
  },
  errorBox: {
    backgroundColor: 'rgba(255, 68, 68, 0.1)',
    borderWidth: 1,
    borderColor: colors.error,
    borderRadius: 8,
    padding: spacing.md,
    marginBottom: spacing.md,
  },
  errorText: {
    color: colors.error,
  },
  loadingContainer: {
    alignItems: 'center',
    padding: spacing.xl,
  },
  loadingText: {
    color: colors.textSecondary,
    marginTop: spacing.md,
  },
  questionCard: {
    backgroundColor: colors.surface,
    borderRadius: 12,
    padding: spacing.lg,
    borderWidth: 1,
    borderColor: colors.border,
  },
  skillName: {
    fontSize: fontSize.lg,
    fontWeight: '600',
    color: colors.text,
    marginBottom: spacing.sm,
  },
  difficultyBadge: {
    backgroundColor: colors.primaryDark,
    paddingHorizontal: spacing.sm,
    paddingVertical: spacing.xs,
    borderRadius: 4,
    alignSelf: 'flex-start',
    marginBottom: spacing.lg,
  },
  difficultyText: {
    color: colors.text,
    fontSize: fontSize.xs,
    fontWeight: '500',
  },
  questionContainer: {
    backgroundColor: colors.background,
    borderRadius: 8,
    padding: spacing.md,
    marginBottom: spacing.lg,
  },
  answerSection: {
    borderTopWidth: 1,
    borderTopColor: colors.border,
    paddingTop: spacing.lg,
  },
  label: {
    fontSize: fontSize.sm,
    fontWeight: '500',
    color: colors.text,
    marginBottom: spacing.sm,
  },
  input: {
    backgroundColor: colors.background,
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: 8,
    padding: spacing.md,
    fontSize: fontSize.lg,
    color: colors.text,
    marginBottom: spacing.md,
  },
  submitButton: {
    backgroundColor: colors.primary,
    borderRadius: 8,
    padding: spacing.md,
    alignItems: 'center',
  },
  buttonDisabled: {
    opacity: 0.5,
  },
  submitButtonText: {
    color: colors.text,
    fontSize: fontSize.md,
    fontWeight: '600',
  },
  emptyState: {
    alignItems: 'center',
    padding: spacing.xl,
  },
  emptyText: {
    color: colors.textSecondary,
    marginBottom: spacing.md,
  },
  button: {
    backgroundColor: colors.primary,
    borderRadius: 8,
    padding: spacing.md,
    paddingHorizontal: spacing.lg,
  },
  buttonText: {
    color: colors.text,
    fontWeight: '600',
  },
  tip: {
    textAlign: 'center',
    color: colors.textMuted,
    fontSize: fontSize.sm,
    marginTop: spacing.xl,
  },
  // Modal styles
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.8)',
    justifyContent: 'center',
    padding: spacing.lg,
  },
  feedbackCard: {
    backgroundColor: colors.surface,
    borderRadius: 16,
    overflow: 'hidden',
  },
  feedbackHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    padding: spacing.lg,
    gap: spacing.sm,
  },
  correctHeader: {
    backgroundColor: 'rgba(179, 255, 0, 0.2)',
  },
  incorrectHeader: {
    backgroundColor: 'rgba(255, 68, 68, 0.2)',
  },
  feedbackEmoji: {
    fontSize: 24,
    color: colors.text,
  },
  feedbackTitle: {
    fontSize: fontSize.xl,
    fontWeight: 'bold',
    color: colors.text,
  },
  feedbackBody: {
    padding: spacing.lg,
  },
  answerRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: spacing.md,
  },
  answerLabel: {
    color: colors.textSecondary,
  },
  answerValue: {
    color: colors.text,
    fontWeight: '500',
  },
  correctAnswer: {
    color: colors.success,
  },
  stepsContainer: {
    marginTop: spacing.md,
    padding: spacing.md,
    backgroundColor: colors.background,
    borderRadius: 8,
  },
  stepsTitle: {
    color: colors.textSecondary,
    fontSize: fontSize.sm,
    marginBottom: spacing.md,
  },
  stepItem: {
    marginBottom: spacing.sm,
  },
  continueButton: {
    backgroundColor: colors.primary,
    padding: spacing.md,
    alignItems: 'center',
    margin: spacing.lg,
    marginTop: 0,
    borderRadius: 8,
  },
  continueButtonText: {
    color: colors.text,
    fontSize: fontSize.md,
    fontWeight: '600',
  },
});
