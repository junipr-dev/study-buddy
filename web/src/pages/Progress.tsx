import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';
import { evaluationAPI } from '../api/evaluation';
import type { LatestEvaluationResponse, EvaluationSummary } from '../api/evaluation';

export default function Progress() {
  const { user } = useAuthStore();
  const navigate = useNavigate();

  const [latestData, setLatestData] = useState<LatestEvaluationResponse | null>(null);
  const [history, setHistory] = useState<EvaluationSummary[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!user) {
      navigate('/login');
      return;
    }

    const fetchData = async () => {
      setIsLoading(true);
      try {
        const [latest, historyData] = await Promise.all([
          evaluationAPI.getLatest(),
          evaluationAPI.getHistory(10),
        ]);
        setLatestData(latest);
        setHistory(historyData.evaluations);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load progress');
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, [user, navigate]);

  if (!user) return null;

  if (isLoading) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
      </div>
    );
  }

  const latest = latestData?.latest;
  const improvement = latestData?.improvement;

  // Format date for display
  const formatDate = (dateStr: string) => {
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
    });
  };

  return (
    <div className="min-h-screen bg-background safe-area-inset">
      <div className="max-w-3xl mx-auto py-4 sm:py-8 px-3 sm:px-4">
        {/* Header */}
        <header className="bg-surface border border-gray-800 rounded-t-lg px-3 sm:px-6 py-3 sm:py-4">
          <div className="flex flex-col sm:flex-row items-center sm:items-end justify-between gap-3">
            <img src="/logo.png" alt="Study Buddy" className="h-16 sm:h-24" />
            <button onClick={() => navigate('/quiz')} className="btn-secondary w-full sm:w-auto">
              Back to Quiz
            </button>
          </div>
        </header>

        <main className="bg-background px-3 sm:px-6 py-4 sm:py-8 border-x border-b border-gray-800 rounded-b-lg">
          {error && (
            <div className="bg-red-500 bg-opacity-10 border border-red-500 text-red-400 px-4 py-3 rounded-lg mb-6">
              {error}
            </div>
          )}

          {/* No Evaluations Yet */}
          {!latest && (
            <div className="card text-center py-12">
              <div className="text-6xl mb-4">📊</div>
              <h2 className="text-2xl font-bold mb-2">No Evaluations Yet</h2>
              <p className="text-gray-400 mb-6">
                Take your first evaluation to see your progress and identify areas to improve.
              </p>
              <button
                onClick={() => navigate('/quiz')}
                className="btn-primary text-lg px-8"
              >
                Take Evaluation
              </button>
            </div>
          )}

          {/* Latest Evaluation Summary */}
          {latest && (
            <>
              {/* Main Score Card */}
              <div className="card mb-6">
                <div className="flex items-center justify-between mb-4">
                  <div>
                    <p className="text-sm text-gray-400">Latest Evaluation</p>
                    <p className="text-gray-500">{formatDate(latest.completed_at)}</p>
                  </div>
                  {improvement && (
                    <div className={`text-right ${improvement.score_change >= 0 ? 'text-success' : 'text-red-400'}`}>
                      <p className="text-2xl font-bold">
                        {improvement.score_change >= 0 ? '▲' : '▼'} {Math.abs(improvement.score_change)}%
                      </p>
                      <p className="text-sm opacity-75">
                        vs {improvement.days_between} days ago
                      </p>
                    </div>
                  )}
                </div>

                {/* Score Display */}
                <div className="text-center py-6">
                  <p className="text-6xl font-bold bg-gradient-to-r from-[#6B4FFF] to-[#FF6EC7] bg-clip-text text-transparent">
                    {latest.overall_score}%
                  </p>
                  <p className="text-gray-400 mt-2">
                    {latest.total_correct} / {latest.total_questions} correct
                  </p>
                </div>

                {/* Skill Breakdown */}
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 sm:gap-3 mt-4">
                  <div className="bg-success bg-opacity-10 rounded-lg p-3 text-center border border-success border-opacity-30">
                    <p className="text-2xl font-bold text-success">{latest.mastered.length}</p>
                    <p className="text-xs text-gray-400 mt-1">Mastered</p>
                  </div>
                  <div className="bg-blue-500 bg-opacity-10 rounded-lg p-3 text-center border border-blue-500 border-opacity-30">
                    <p className="text-2xl font-bold text-blue-400">{latest.proficient.length}</p>
                    <p className="text-xs text-gray-400 mt-1">Proficient</p>
                  </div>
                  <div className="bg-orange-500 bg-opacity-10 rounded-lg p-3 text-center border border-orange-500 border-opacity-30">
                    <p className="text-2xl font-bold text-orange-400">{latest.developing.length}</p>
                    <p className="text-xs text-gray-400 mt-1">Developing</p>
                  </div>
                  <div className="bg-red-500 bg-opacity-10 rounded-lg p-3 text-center border border-red-500 border-opacity-30">
                    <p className="text-2xl font-bold text-red-400">{latest.study.length}</p>
                    <p className="text-xs text-gray-400 mt-1">Need Study</p>
                  </div>
                </div>
              </div>

              {/* Action Buttons */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4 mb-6">
                <button
                  onClick={() => navigate('/quiz')}
                  className="btn-primary py-3 sm:py-4 text-base sm:text-lg"
                >
                  Take New Evaluation
                </button>
                <button
                  onClick={() => navigate('/quiz?mode=practice')}
                  className="btn-secondary py-3 sm:py-4 text-base sm:text-lg"
                >
                  Practice Weak Areas
                </button>
              </div>

              {/* Areas Needing Study - Failed Level 1 */}
              {latest.study.length > 0 && (
                <div className="card mb-6">
                  <h2 className="text-lg font-semibold mb-4 text-red-400">
                    📚 Priority Study Areas
                  </h2>
                  <div className="space-y-2">
                    {latest.study.slice(0, 5).map((skill) => (
                      <div
                        key={skill.skill_id}
                        className="bg-background p-3 rounded-lg flex items-center justify-between border border-gray-800"
                      >
                        <span>{skill.skill_name}</span>
                        <span className="text-red-400 font-medium">
                          {skill.proficiency_score}%
                        </span>
                      </div>
                    ))}
                    {latest.study.length > 5 && (
                      <p className="text-sm text-gray-500 text-center pt-2">
                        +{latest.study.length - 5} more skills need study
                      </p>
                    )}
                  </div>
                </div>
              )}

              {/* Developing Skills - Passed Level 1 only */}
              {latest.developing.length > 0 && (
                <div className="card mb-6">
                  <h2 className="text-lg font-semibold mb-4 text-orange-400">
                    🌱 Developing Skills
                  </h2>
                  <div className="space-y-2">
                    {latest.developing.slice(0, 5).map((skill) => (
                      <div
                        key={skill.skill_id}
                        className="bg-background p-3 rounded-lg flex items-center justify-between border border-gray-800"
                      >
                        <span>{skill.skill_name}</span>
                        <span className="text-orange-400 font-medium">
                          {skill.proficiency_score}%
                        </span>
                      </div>
                    ))}
                    {latest.developing.length > 5 && (
                      <p className="text-sm text-gray-500 text-center pt-2">
                        +{latest.developing.length - 5} more developing skills
                      </p>
                    )}
                  </div>
                </div>
              )}

              {/* Proficient Skills - Passed Level 2 */}
              {latest.proficient.length > 0 && (
                <div className="card mb-6">
                  <h2 className="text-lg font-semibold mb-4 text-blue-400">
                    💪 Proficient Skills
                  </h2>
                  <div className="flex flex-wrap gap-2">
                    {latest.proficient.map((skill) => (
                      <span
                        key={skill.skill_id}
                        className="bg-blue-500 bg-opacity-10 text-blue-400 px-3 py-1 rounded-full text-sm border border-blue-500 border-opacity-30"
                      >
                        {skill.skill_name}
                      </span>
                    ))}
                  </div>
                </div>
              )}

              {/* Mastered Skills */}
              {latest.mastered.length > 0 && (
                <div className="card mb-6">
                  <h2 className="text-lg font-semibold mb-4 text-success">
                    ✓ Mastered Skills
                  </h2>
                  <div className="flex flex-wrap gap-2">
                    {latest.mastered.map((skill) => (
                      <span
                        key={skill.skill_id}
                        className="bg-success bg-opacity-10 text-success px-3 py-1 rounded-full text-sm border border-success border-opacity-30"
                      >
                        {skill.skill_name}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </>
          )}

          {/* Evaluation History */}
          {history.length > 1 && (
            <div className="card">
              <h2 className="text-lg font-semibold mb-4">Past Evaluations</h2>
              <div className="space-y-3">
                {history.slice(1).map((evaluation) => (
                  <div
                    key={evaluation.id}
                    className="bg-background p-4 rounded-lg flex items-center justify-between border border-gray-800"
                  >
                    <div>
                      <p className="font-medium">{formatDate(evaluation.completed_at)}</p>
                      <p className="text-sm text-gray-400">
                        {evaluation.total_correct}/{evaluation.total_questions} correct •{' '}
                        {evaluation.skills_mastered} mastered
                      </p>
                    </div>
                    <div className="text-right">
                      <p className="text-2xl font-bold">{evaluation.overall_score}%</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Improvement Chart Placeholder */}
          {history.length > 1 && (
            <div className="card mt-6">
              <h2 className="text-lg font-semibold mb-4">Your Journey</h2>
              <div className="flex items-end justify-between h-32 px-4">
                {history.slice().reverse().slice(-6).map((evaluation) => (
                  <div key={evaluation.id} className="flex flex-col items-center">
                    <div
                      className="w-8 bg-gradient-to-t from-[#6B4FFF] to-[#FF6EC7] rounded-t"
                      style={{ height: `${evaluation.overall_score}%` }}
                    />
                    <p className="text-xs text-gray-500 mt-2">
                      {new Date(evaluation.completed_at).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}
                    </p>
                  </div>
                ))}
              </div>
            </div>
          )}
        </main>
      </div>
    </div>
  );
}
