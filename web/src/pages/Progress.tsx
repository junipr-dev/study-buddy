import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';
import { progressAPI } from '../api/progress';
import type { ProgressSummary, WeakArea } from '../types';

export default function Progress() {
  const { user } = useAuthStore();
  const navigate = useNavigate();

  const [summary, setSummary] = useState<ProgressSummary | null>(null);
  const [weakAreas, setWeakAreas] = useState<WeakArea[]>([]);
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
        const [summaryData, weakAreasData] = await Promise.all([
          progressAPI.getSummary(),
          progressAPI.getWeakAreas(),
        ]);
        setSummary(summaryData);
        setWeakAreas(weakAreasData);
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

  if (error || !summary) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <div className="text-red-400">{error || 'Failed to load progress'}</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-background">
      <div className="max-w-3xl mx-auto py-8 px-4">
        {/* Header */}
        <header className="bg-surface border border-gray-800 rounded-t-lg px-6 py-4">
          <div className="flex items-center justify-between">
            <h1 className="text-2xl font-bold bg-gradient-to-r from-[#6B4FFF] to-[#FF6EC7] bg-clip-text text-transparent">Your Progress</h1>
            <button onClick={() => navigate('/quiz')} className="btn-primary">
              Continue Practicing
            </button>
          </div>
        </header>

        <main className="bg-background px-6 py-8 border-x border-b border-gray-800 rounded-b-lg">
        {/* Overall Stats */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
          <div className="card">
            <p className="text-sm text-gray-400 mb-1">Questions Answered</p>
            <p className="text-3xl font-bold text-primary">{summary.total_questions_answered}</p>
          </div>
          <div className="card">
            <p className="text-sm text-gray-400 mb-1">Overall Accuracy</p>
            <p className="text-3xl font-bold text-success">{summary.overall_accuracy.toFixed(1)}%</p>
          </div>
          <div className="card">
            <p className="text-sm text-gray-400 mb-1">Skills Practiced</p>
            <p className="text-3xl font-bold">{summary.skills_practiced}</p>
          </div>
          <div className="card">
            <p className="text-sm text-gray-400 mb-1">Skills Mastered</p>
            <p className="text-3xl font-bold text-success">{summary.skills_mastered}</p>
          </div>
        </div>

        {/* Progress Breakdown */}
        <div className="card mb-8">
          <h2 className="text-xl font-semibold mb-4">Mastery Breakdown</h2>
          <div className="grid grid-cols-3 gap-4">
            <div>
              <p className="text-sm text-gray-400 mb-2">Mastered (≥90%)</p>
              <div className="bg-success bg-opacity-20 rounded-lg p-4 text-center">
                <p className="text-2xl font-bold text-success">{summary.skills_mastered}</p>
              </div>
            </div>
            <div>
              <p className="text-sm text-gray-400 mb-2">In Progress (50-89%)</p>
              <div className="bg-secondary bg-opacity-20 rounded-lg p-4 text-center">
                <p className="text-2xl font-bold text-secondary">{summary.skills_in_progress}</p>
              </div>
            </div>
            <div>
              <p className="text-sm text-gray-400 mb-2">Need Work (&lt;50%)</p>
              <div className="bg-red-500 bg-opacity-20 rounded-lg p-4 text-center">
                <p className="text-2xl font-bold text-red-400">{summary.skills_weak}</p>
              </div>
            </div>
          </div>
        </div>

        {/* Weak Areas */}
        {weakAreas.length > 0 && (
          <div className="card">
            <h2 className="text-xl font-semibold mb-4">Areas Needing Attention</h2>
            <div className="space-y-3">
              {weakAreas.map((area) => (
                <div
                  key={area.skill_id}
                  className="bg-background p-4 rounded-lg border border-gray-800"
                >
                  <div className="flex items-center justify-between mb-2">
                    <div>
                      <h3 className="font-medium">{area.skill_name}</h3>
                      <p className="text-sm text-gray-400">{area.subject}</p>
                    </div>
                    <div className="text-right">
                      <p className="text-sm text-gray-400">Mastery</p>
                      <p className="text-lg font-bold text-red-400">
                        {area.mastery_score.toFixed(0)}%
                      </p>
                    </div>
                  </div>
                  {area.is_prerequisite_gap && (
                    <div className="mt-2 text-sm">
                      <p className="text-yellow-400">
                        ⚠️ Prerequisite Gap - This affects: {area.dependent_skills.join(', ')}
                      </p>
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Skills List */}
        <div className="card mt-8">
          <h2 className="text-xl font-semibold mb-4">All Skills</h2>
          <div className="space-y-2">
            {summary.mastery_by_skill.map((mastery) => (
              <div
                key={mastery.skill_id}
                className="bg-background p-3 rounded-lg flex items-center justify-between"
              >
                <div>
                  <h3 className="font-medium">{mastery.skill_name}</h3>
                  <p className="text-sm text-gray-400">
                    {mastery.subject} • {mastery.total_attempts} attempts
                  </p>
                </div>
                <div className="text-right">
                  <p className="text-lg font-bold">{mastery.mastery_score.toFixed(0)}%</p>
                  <div className="w-24 h-2 bg-gray-800 rounded-full mt-1 overflow-hidden">
                    <div
                      className={`h-full rounded-full ${
                        mastery.mastery_score >= 90
                          ? 'bg-success'
                          : mastery.mastery_score >= 50
                          ? 'bg-secondary'
                          : 'bg-red-500'
                      }`}
                      style={{ width: `${mastery.mastery_score}%` }}
                    />
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
        </main>
      </div>
    </div>
  );
}
