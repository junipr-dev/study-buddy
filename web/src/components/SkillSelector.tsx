import { useEffect, useState } from 'react';
import { api } from '../api/client';

interface Skill {
  id: number;
  slug: string;
  name: string;
  subject: string;
  description: string;
  difficulty_base: number;
}

interface SkillSelectorProps {
  onSelectSkill: (skillId: number | null) => void;
  selectedSkillId: number | null;
}

export default function SkillSelector({ onSelectSkill, selectedSkillId }: SkillSelectorProps) {
  const [skills, setSkills] = useState<Skill[]>([]);
  const [isOpen, setIsOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    fetchSkills();
  }, []);

  const fetchSkills = async () => {
    try {
      const response = await api.get<{ skills: Skill[] }>('/skills');
      setSkills(response.skills);
    } catch (error) {
      console.error('Failed to fetch skills:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const groupedSkills = skills.reduce((acc, skill) => {
    if (!acc[skill.subject]) {
      acc[skill.subject] = [];
    }
    acc[skill.subject].push(skill);
    return acc;
  }, {} as Record<string, Skill[]>);

  const selectedSkill = skills.find(s => s.id === selectedSkillId);

  if (isLoading) {
    return (
      <div className="mb-6">
        <div className="animate-pulse bg-surface rounded-lg h-12"></div>
      </div>
    );
  }

  return (
    <div className="mb-6">
      <div className="relative">
        <button
          onClick={() => setIsOpen(!isOpen)}
          className="w-full px-4 py-3 bg-surface border-2 border-gray-700 rounded-lg flex items-center justify-between hover:border-primary transition-all"
        >
          <div className="text-left">
            <div className="text-xs text-gray-500 mb-1">Practice Mode</div>
            <div className="font-medium">
              {selectedSkill ? selectedSkill.name : 'Adaptive (Recommended)'}
            </div>
            {selectedSkill && (
              <div className="text-xs text-gray-400 mt-1">{selectedSkill.subject}</div>
            )}
          </div>
          <svg
            className={`w-5 h-5 text-gray-400 transition-transform ${isOpen ? 'rotate-180' : ''}`}
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        </button>

        {isOpen && (
          <div className="absolute z-10 w-full mt-2 bg-surface border-2 border-gray-700 rounded-lg shadow-2xl max-h-96 overflow-y-auto">
            <button
              onClick={() => {
                onSelectSkill(null);
                setIsOpen(false);
              }}
              className={`w-full px-4 py-3 text-left hover:bg-primary hover:bg-opacity-10 transition-all border-b border-gray-800 ${
                !selectedSkillId ? 'bg-primary bg-opacity-20' : ''
              }`}
            >
              <div className="font-medium">Adaptive Mode</div>
              <div className="text-xs text-gray-400 mt-1">
                Let the algorithm choose the best skill for you
              </div>
            </button>

            {Object.entries(groupedSkills).map(([subject, subjectSkills]) => (
              <div key={subject}>
                <div className="px-4 py-2 bg-background text-xs font-semibold text-gray-500 sticky top-0">
                  {subject}
                </div>
                {subjectSkills.map(skill => (
                  <button
                    key={skill.id}
                    onClick={() => {
                      onSelectSkill(skill.id);
                      setIsOpen(false);
                    }}
                    className={`w-full px-4 py-3 text-left hover:bg-primary hover:bg-opacity-10 transition-all border-b border-gray-800 last:border-b-0 ${
                      selectedSkillId === skill.id ? 'bg-primary bg-opacity-20' : ''
                    }`}
                  >
                    <div className="font-medium">{skill.name}</div>
                    <div className="text-xs text-gray-400 mt-1">
                      {skill.description}
                    </div>
                    <div className="flex items-center gap-2 mt-1">
                      <span className="text-xs text-gray-500">
                        Difficulty: {skill.difficulty_base}/5
                      </span>
                    </div>
                  </button>
                ))}
              </div>
            ))}
          </div>
        )}
      </div>

      {selectedSkill && (
        <div className="mt-2 text-xs text-gray-500 text-center">
          You're practicing a specific skill. Switch to Adaptive Mode to let the algorithm choose for you.
        </div>
      )}
    </div>
  );
}
